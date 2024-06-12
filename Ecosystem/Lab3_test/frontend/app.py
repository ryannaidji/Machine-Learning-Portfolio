import streamlit as st
import requests
from pydantic import BaseModel, ValidationError

def main():
    # Tables de correspondance pour la classification
    star_labels = {
        0: "Naine Brune",
        1: "Séquence principale",
        2: "Naine blanche",
        3: "Supergéante",
        4: "Hypergéante",
        5: "Géante"
    }

    # URL de base de l'API FastAPI
    BASE_API_URL = "http://backend:8000/predict"

    # Définir la classe de validation des caractéristiques des étoiles
    class StarFeatures(BaseModel):
        temperature: float
        luminosity: float
        radius: float
        magnitude: float
        star_color: str
        spectral_class: str

    st.sidebar.title("Source du Dataset")
    st.sidebar.markdown("**[Cliquez ici pour accéder au dataset](https://www.kaggle.com/datasets/deepu1109/star-dataset)**")
    st.sidebar.header("Développé par **`Ryan NAIDJI`**")

    st.title("Classification d'étoiles avec MLflow, FastAPI et Streamlit")

    st.header("Objectif du projet")
    st.markdown("""
    Ce projet vise à démontrer l'intégration efficace de plusieurs technologies avancées dans le domaine du développement et du déploiement de modèles de machine learning. Nous utilisons **MLflow** pour la gestion des modèles et des expériences, **FastAPI** pour créer une API performante, **Streamlit** pour l'interface utilisateur interactive, et **Docker-compose** pour le déploiement conteneurisé et la reproductibilité des environnements.
    """)

    st.subheader("À propos de la classification des étoiles")
    st.write("""
    Le but de ce projet est de classifier les types d'étoiles en utilisant des caractéristiques telles que la température, la luminosité, et le rayon. Les utilisateurs peuvent entrer les spécifications d'une étoile et voir comment elle est classée en fonction des données fournies.
    """)

    st.subheader("Comprendre la classification des étoiles avec le diagramme de Hertzsprung-Russell")
    st.markdown("""
    Le diagramme de Hertzsprung-Russell est un outil crucial en astrophysique pour classer les étoiles en fonction de leur luminosité et température de surface. Sur ce diagramme :
    - L'axe horizontal représente la température de surface de l'étoile, diminuant de gauche à droite.
    - L'axe vertical représente la luminosité de l'étoile, mesurée en unités solaires.
    - Les différentes zones du diagramme représentent différents types d'étoiles, tels que les naines blanches, les géantes rouges et les étoiles de la séquence principale.
    """)

    # Charger et afficher l'image du diagramme HR
    st.image("./class.jpg", caption="Diagramme de Hertzsprung-Russell")

    st.subheader("Technologies utilisées")
    st.markdown("""
    - **MLflow** : Utilisé pour tracer, gérer, inspecter et organiser les travaux de machine learning, permettant une expérimentation systématique.
    - **FastAPI** : Fournit une interface pour interroger nos modèles de machine learning de manière rapide et avec peu de latence, en utilisant une API REST.
    - **Streamlit** : Permet la création d'une interface utilisateur interactive pour la visualisation des données et des résultats de classification.
    - **Docker-compose** : Facilite le déploiement de notre application en conteneurs, assurant la cohérence des environnements entre le développement et la production.
    """)

    # Entrée des caractéristiques des étoiles
    col1, col2 = st.columns(2)
    with col1:
        temp = st.number_input("Température (K)", min_value=2000, max_value=50000, value=5500, step=100)
        lum = st.number_input("Luminosité (L/Lo)", min_value=0.0001, max_value=100000.0, value=1.0, step=0.1)
        rad = st.number_input("Rayon (R/Ro)", min_value=0.01, max_value=100.0, value=1.0, step=0.01)
    with col2:
        mag = st.number_input("Magnitude absolue (Mv)", min_value=-30, max_value=15, value=5, step=1)
        color = st.selectbox("Couleur de l'étoile", options=['Blue', 'Blue White', 'Orange', 'Orange Red', 'Pale Yellow Orange', 'Red', 'White', 'Whitish', 'Yellowish', 'Yellowish White'])
        spectral_class = st.selectbox('Classe spectrale', options=['A', 'B', 'F', 'G', 'K', 'M', 'O'])

    model_choice = st.selectbox('Choisissez le modèle de machine learning', options=['Logistic Regression', 'Random Forest', 'SVC', 'Decision Tree'])

    if st.button("Classer l'étoile"):
        # Préparer les données pour l'API
        star_data = {
            "temperature": temp,
            "luminosity": lum,
            "radius": rad,
            "magnitude": mag,
            "star_color": color,
            "spectral_class": spectral_class
        }

        model_name = model_choice.lower().replace(" ", "_")

        # Envoyer les données à l'API FastAPI
        try:
            response = requests.post(f"{BASE_API_URL}/{model_name}", json=star_data)
            if response.status_code == 200:
                prediction = response.json()
                star_type = star_labels.get(prediction['prediction'], "Type inconnu")
                st.success(f"Résultat de la classification : **{star_type}**")
            else:
                st.error(f"Erreur dans la réponse de l'API : {response.text}")
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
