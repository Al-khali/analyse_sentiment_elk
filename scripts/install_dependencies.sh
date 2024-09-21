#!/bin/bash

# Script pour installer les dépendances Python

# Mise à jour de pip
pip install --upgrade pip

# Installation des dépendances à partir du fichier requirements.txt
pip install -r requirements.txt

echo "Installation des dépendances Python terminée."