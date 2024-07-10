# TP3 - Classification du type d'une étoile en utilisant MLflow, Streamlit, FastAPI et Docker-compose

## Description du projet

Ce projet a pour but de développer plusieurs modèles capable de classer le type d'une étoile en prenant en compte plusieurs de ses caractéristiques. Le tout en utilisant Streamlit pour le frontend, FastAPI pour le backend, MLflow pour la gestion des modèles et Docker-compose pour l'orchestration du déploiement du projet.

## Installation des dépendances

Les dépendances sont inclues dans un fichier requirements.txt. Un fichier très basique avec les dépendances nécessaires au bon fonctionnement de l'application, comme mlflow, scikit-learn, numpy, pandas, fastapi, uvicorn et streamlit.

## Utilisation

Afin de s'assurer du bon fonctionnement du projet, vous devez d'abord créer vos modèles grâce à MLflow, ensuite vous devrez entrer manuellement le `experiment_id` les `run_id` dans le fichier "main.py" du backend. Une fois que vos modèles sont créés, il ne vous manque plus qu'a construire votre image et à la monter avec la commande 

```bash
"docker-compose up --build"
```

### MLflow

Nous utilisons mlflow pour la gestion des modèles. Un fichier model_t.py est concu spécialement pour enregistrer les différents modèles qu'on utilisera (algorithmes d'apprentissage supervisé), tel que SVC, RandomForest, régression logistique, DecisionTreeClassifier entraînés à partir d'un dataset trouvé sur Kaggle. Un pipeline est enregistré pour chaque modèle incluant un prétraitement des données.

À noter que notre objectif est de se concentrer sur le déploiement et l'orchestration. Les modèles ne sont pas optimisés et certains sont en surapprentissage.

### FastAPI

FastAPI est notre pilier du backend, il permet de faire des requêtes API et d'utiliser les modèles du registre de modèle de MLflow. Il y a seulement une fonction pour une requête API "POST", qui nous permettra de faire des prédictions sur plusieurs modèles.

### Streamlit

Streamlit nous sert de frontend. C'est ici que l'utilisateur entrera ses données pour classer son étoile et qu'il recevra la classe de l'étoile selon différents modèles. Il contient aussi une petite description du projet.

### Docker

Nous utilisons Docker pour le déploiement. Tout d'abord nous avons 2 fichiers Dockerfile donc 2 conteneurs, un pour le backend et un pour le frontend. Ensuite nous avons un fichier docker-compose.yml, qui s'occupera de l'orchestration lors du déploiement. Dans notre cas, nous nous assurons que FastAPI est opérationnel pour démarrer Streamlit.

