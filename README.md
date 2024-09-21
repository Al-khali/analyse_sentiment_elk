# Projet d'Analyse de Sentiment avec ELK

Ce projet vise à collecter des données depuis les réseaux sociaux, effectuer une analyse de sentiment en temps réel, et visualiser les résultats à l'aide de la stack ELK (Elasticsearch, Logstash, Kibana).

## Structure du Projet

```
projet_analyse_sentiment_elk/
├── scripts/
├── src/
│   ├── data_collection/
│   ├── data_processing/
│   ├── data_storage/
│   ├── monitoring/
│   └── visualization/
├── config/
├── data/
├── logs/
└── tests/
```

## Installation

1. Clonez ce dépôt
2. Exécutez `scripts/install_dependencies.sh` pour installer les dépendances
3. Configurez les fichiers dans le dossier `config/`

## Utilisation

1. Démarrez les services avec `scripts/start_services.sh`
2. Exécutez le script principal : `python src/main.py`
3. Accédez à Kibana pour visualiser les résultats

## Contribution

Les pull requests sont les bienvenues. Pour les changements majeurs, veuillez d'abord ouvrir une issue pour discuter de ce que vous aimeriez changer.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
