# Projet ELK - Scraping et Analyse de Sentiment

Ce projet répond aux exigences du test technique ELK - Scraping. Il met en place une stack ELK (Elasticsearch, Logstash, Kibana) avec des fonctionnalités de scraping de réseaux sociaux et d'analyse de sentiment.

## Table des matières
1. [Installation d'ELK](#installation-delk)
2. [Configuration d'ELK](#configuration-delk)
3. [Scraping et Analyse de Sentiment](#scraping-et-analyse-de-sentiment)
4. [Structure du Projet](#structure-du-projet)
5. [Installation et Utilisation](#installation-et-utilisation)

## Installation d'ELK

Pour installer ELK sur une VM Linux :

1. Si vous n'avez pas d'OS Linux, utilisez VirtualBox pour créer une VM Linux.
2. Exécutez le script d'installation :

```bash
./scripts/install_elk.sh
```

Ce script installe Elasticsearch, Logstash et Kibana sur votre système.

## Configuration d'ELK

### Authentification et Personnalisation

1. Pour ajouter l'authentification et changer le logo de Kibana, exécutez :

```bash
./scripts/configure_elk.sh
```

Ce script :
- Configure l'authentification pour ELK (login et mot de passe)
- Remplace le logo de Kibana par un logo personnalisé (situé dans `assets/custom_logo.png`)

### Intégration de l'Analyse de Sentiment

L'analyse de sentiment est intégrée via un service Python utilisant VADER. Le pipeline Logstash est configuré pour utiliser ce service.

1. Lancez le service d'analyse de sentiment :

```bash
python src/sentiment_analysis/sentiment_service.py
```

2. Le pipeline Logstash (`config/logstash_pipeline.conf`) est déjà configuré pour utiliser ce service.

## Scraping et Analyse de Sentiment

### Collecte de Données

Les scripts de scraping pour Facebook et Instagram sont situés dans `src/data_collection/`. Ils collectent des posts liés à un sujet spécifique (par exemple, "le décès du président Jacques Chirac").

Pour exécuter le scraping :

```bash
python src/data_collection/facebook_scraper.py
python src/data_collection/instagram_scraper.py
```

### Stockage dans MongoDB

Les données collectées sont automatiquement stockées dans MongoDB. La configuration de connexion est dans `src/data_storage/mongodb_handler.py`.

## Structure du Projet

```
elk-scraping-project/
├── scripts/
│   ├── install_elk.sh
│   └── configure_elk.sh
├── config/
│   ├── elasticsearch.yml
│   ├── kibana.yml
│   └── logstash_pipeline.conf
├── src/
│   ├── sentiment_analysis/
│   ├── data_collection/
│   └── data_storage/
├── assets/
│   └── custom_logo.png
├── requirements.txt
└── README.md
```

## Installation et Utilisation

1. Clonez ce dépôt
2. Installez les dépendances : `pip install -r requirements.txt`
3. Suivez les étapes d'installation et de configuration d'ELK ci-dessus
4. Lancez le service d'analyse de sentiment
5. Exécutez les scripts de scraping
6. Utilisez Kibana pour visualiser et analyser les données


# Améliorations Potentielles

1. **Scraping Robuste**:
   - Utiliser Scrapfly pour contourner les CAPTCHAs et améliorer la fiabilité du scraping.
   - Intégrer des bibliothèques spécialisées comme 'instagram-scraper' pour Instagram et 'facebook-scraper' pour Facebook.

2. **Intégration d'APIs**:
   - Implémenter 'google-api-python-client' pour interagir avec l'API Google, élargissant les sources de données.

3. **Optimisation de la Base de Données**:
   - Utiliser 'pymongo' pour une interaction plus efficace avec MongoDB.

4. **Analyse de Sentiment Avancée**:
   - Intégrer 'vaderSentiment' pour une analyse de sentiment plus précise et nuancée.

5. **Containerisation**:
   - Dockeriser l'application pour faciliter le déploiement et la scalabilité.

6. **Intégration Continue**:
   - Mettre en place des webhooks pour une récupération en temps réel des données d'analyse de sentiment.

7. **Automatisation des Tâches**:
   - Utiliser 'schedule' pour planifier et automatiser les tâches récurrentes.

8. **Gestion de Configuration**:
   - Implémenter 'PyYAML' pour une gestion plus flexible des fichiers de configuration.

9. **Optimisation ELK**:
   - Utiliser 'elasticsearch-dsl' pour des requêtes Elasticsearch plus puissantes et lisibles.
   - Intégrer des bibliothèques spécifiques pour Kibana et Logstash pour une meilleure gestion des visualisations et des logs.

10. **Sécurité et Performance**:
    - Renforcer la sécurité des données et optimiser les performances du pipeline de traitement.

11. **Tests et Monitoring**:
    - Implémenter des tests unitaires et d'intégration.
    - Mettre en place un système de monitoring pour surveiller la santé de l'application.


---

Ce projet répond à toutes les exigences du test technique, en mettant en place une stack ELK fonctionnelle avec scraping de réseaux sociaux, analyse de sentiment, et stockage dans MongoDB.