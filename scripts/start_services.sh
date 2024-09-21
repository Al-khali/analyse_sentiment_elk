#!/bin/bash

# Script pour démarrer les services ELK

# Démarrage d'Elasticsearch
sudo systemctl start elasticsearch
# Attente que Elasticsearch soit complètement démarré
while ! curl -s http://localhost:9200 >/dev/null; do
    sleep 1
done

# Démarrage de Kibana
sudo systemctl start kibana

# Démarrage de Logstash
sudo systemctl start logstash

echo "Services ELK démarrés."