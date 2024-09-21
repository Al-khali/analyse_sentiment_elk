#!/bin/bash

# Script pour installer Elasticsearch, Logstash et Kibana

# Mise à jour des paquets
sudo apt update
sudo apt upgrade -y

# Installation de Java (prérequis pour ELK)
sudo apt install openjdk-11-jdk -y

# Ajout du référentiel Elastic
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

# Mise à jour des paquets après l'ajout du référentiel
sudo apt update

# Installation d'Elasticsearch
sudo apt install elasticsearch -y

# Installation de Logstash
sudo apt install logstash -y

# Installation de Kibana
sudo apt install kibana -y

echo "Installation d'ELK terminée."