#!/bin/bash

# Script pour configurer Elasticsearch, Logstash et Kibana

# Création d'un utilisateur et mot de passe pour ELK
ELASTIC_PASSWORD=$(openssl rand -base64 16)
echo "Mot de passe généré pour ELK: $ELASTIC_PASSWORD"

# Configuration d'Elasticsearch avec authentification
sudo tee -a /etc/elasticsearch/elasticsearch.yml > /dev/null <<EOT
network.host: 0.0.0.0
discovery.type: single-node
xpack.security.enabled: true
EOT

# Définition du mot de passe pour l'utilisateur 'elastic'
echo "y" | sudo /usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive <<EOF
$ELASTIC_PASSWORD
$ELASTIC_PASSWORD
$ELASTIC_PASSWORD
$ELASTIC_PASSWORD
$ELASTIC_PASSWORD
$ELASTIC_PASSWORD
EOF

# Configuration de Kibana avec authentification
sudo tee -a /etc/kibana/kibana.yml > /dev/null <<EOT
server.host: "0.0.0.0"
elasticsearch.hosts: ["http://localhost:9200"]
elasticsearch.username: "kibana_system"
elasticsearch.password: "$ELASTIC_PASSWORD"
EOT

# Changement du logo Kibana
sudo cp ~/Téléchargements/logo.svg /usr/share/kibana/src/core/server/core_app/assets/logo.svg

# Configuration de base de Logstash avec authentification
sudo tee /etc/logstash/conf.d/logstash.conf > /dev/null <<EOT
input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    user => "elastic"
    password => "$ELASTIC_PASSWORD"
    index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
  }
}
EOT

# Redémarrage des services pour appliquer les configurations
sudo systemctl restart elasticsearch
sudo systemctl restart kibana
sudo systemctl restart logstash

echo "Configuration d'ELK terminée avec authentification et nouveau logo."