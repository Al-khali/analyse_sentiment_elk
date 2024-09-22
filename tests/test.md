# Procédures de Test pour le Projet ELK-Scraping

Ce document décrit les procédures de test pour le projet ELK-Scraping, couvrant l'installation d'ELK, la configuration, le scraping de données, l'analyse de sentiment, et le stockage dans MongoDB.

## Table des matières
1. [Prérequis](#prérequis)
2. [Configuration de l'environnement de test](#configuration-de-lenvironnement-de-test)
3. [Exécution des tests unitaires](#exécution-des-tests-unitaires)
4. [Tests d'intégration](#tests-dintégration)
5. [Tests de performance](#tests-de-performance)
6. [Validation manuelle](#validation-manuelle)

## Prérequis

- Python 3.7+
- pytest
- MongoDB installé et en cours d'exécution
- ELK stack (Elasticsearch, Logstash, Kibana) installée
- Accès Internet pour les tests de scraping (ou des mocks configurés)

## Configuration de l'environnement de test

1. Clonez le dépôt :
   ```
   git clone https://github.com/al-khali/elk-scraping-project.git
   cd elk-scraping-project
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Assurez-vous que MongoDB est en cours d'exécution sur `localhost:27017`

4. Configurez un fichier `.env` à la racine du projet avec les credentials nécessaires (si applicable pour les tests) :
   ```
   FACEBOOK_ACCESS_TOKEN=votre_token_de_test
   INSTAGRAM_USERNAME=votre_username_de_test
   INSTAGRAM_PASSWORD=votre_password_de_test
   ```

## Exécution des tests unitaires

Exécutez les tests unitaires avec pytest :

```
pytest tests/
```

### Description des tests unitaires

1. `test_data_storage.py` : Teste les opérations CRUD sur MongoDB.
2. `test_scraper.py` : Vérifie le fonctionnement des scrapers Facebook et Instagram.
3. `test_sentiment_analyzer.py` : Valide l'analyse de sentiment pour différents types de textes.

## Tests d'intégration

1. Test d'intégration ELK :
   - Lancez Elasticsearch, Logstash, et Kibana.
   - Vérifiez que Logstash peut envoyer des données à Elasticsearch.
   - Confirmez que Kibana peut se connecter à Elasticsearch et afficher les données.

2. Test du flux complet :
   - Exécutez les scripts de scraping.
   - Vérifiez que les données sont correctement stockées dans MongoDB.
   - Confirmez que l'analyse de sentiment est effectuée sur les données collectées.
   - Assurez-vous que les données analysées sont correctement indexées dans Elasticsearch.
   - Visualisez les résultats dans Kibana.

## Tests de performance

1. Test de charge du scraping :
   - Exécutez les scrapers avec un grand nombre de requêtes (par exemple, 1000 posts).
   - Mesurez le temps d'exécution et la consommation de ressources.

2. Test de performance d'Elasticsearch :
   - Indexez un grand volume de données (par exemple, 100 000 documents).
   - Effectuez des requêtes complexes et mesurez le temps de réponse.

3. Test de performance de l'analyse de sentiment :
   - Analysez un grand nombre de textes (par exemple, 10 000).
   - Mesurez le temps moyen d'analyse par texte.

## Validation manuelle

1. Vérification de l'installation d'ELK :
   - Confirmez que l'authentification fonctionne correctement.
   - Vérifiez que le logo personnalisé est bien affiché dans Kibana.

2. Validation des données scrapées :
   - Examinez manuellement un échantillon de données collectées pour s'assurer de leur pertinence et exactitude.

3. Vérification de l'analyse de sentiment :
   - Sélectionnez un échantillon de textes et comparez les résultats de l'analyse automatique avec une évaluation manuelle.

4. Test de l'interface Kibana :
   - Créez manuellement quelques visualisations et tableaux de bord.
   - Vérifiez que les filtres et les recherches fonctionnent comme prévu.

## Rapport de test

Après avoir exécuté tous les tests, créez un rapport détaillant :
- Les résultats des tests unitaires
- Les observations des tests d'intégration et de performance
- Les résultats de la validation manuelle
- Toute anomalie ou bogue découvert
- Suggestions d'amélioration ou d'optimisation

## Notes

- Certains tests, notamment ceux impliquant des API externes, peuvent nécessiter des mocks ou des environnements de test spécifiques.
- Assurez-vous de respecter les limites d'utilisation des API lors des tests de performance.
- La validation manuelle est cruciale pour garantir la qualité globale du projet au-delà des tests automatisés.