#!/bin/bash

# Script pour arrêter les services ELK

# Arrêt de Logstash
sudo systemctl stop logstash

# Arrêt de Kibana
sudo systemctl stop kibana

# Arrêt d'Elasticsearch
sudo systemctl stop elasticsearch

echo "Services ELK arrêtés."