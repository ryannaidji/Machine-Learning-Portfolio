from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
import mlflow.pyfunc
import numpy as np

app = FastAPI()

class StarFeatures(BaseModel):
    temperature: float  # Température en Kelvin
    luminosity: float   # Luminosité en L/Lo
    radius: float       # Rayon en R/Ro
    magnitude: float    # Magnitude absolue
    star_color: str     # Couleur de l'étoile
    spectral_class: str # Classe spectrale

# Dictionnaire pour mapper les noms des modèles aux identifiants de run correspondants
model_run_ids = {
    "logistic_regression": "af60168c64224a4bbde09b2d247b45f7",
    "random_forest": "e0f9ec9f915845eba4da98017b74fee4",
    "svc": "a57219c48f00448d9d5721a9435a9d03",
    "decision_tree": "8f551d16e6c94abfa8b3a547379df039"
}

experiment_id = "340660044929466591"
#run_id = "eed407e7511445c9a20807a911e838b9"
#model_path = f"/app/mlruns/{experiment_id}/{run_id}/artifacts/model"
#model = mlflow.pyfunc.load_model(model_path)

@app.post("/predict/{model_name}")
def predict(model_name: str, features: StarFeatures):
    # Vérifier si le modèle existe
    if model_name not in model_run_ids:
        raise HTTPException(status_code=404, detail="Modèle non trouvé")
    
    run_id = model_run_ids[model_name]
    model_path = f"/app/mlruns/{experiment_id}/{run_id}/artifacts/model"
    model = mlflow.pyfunc.load_model(model_path)

    # Créer un DataFrame à partir des caractéristiques avec les noms de colonnes appropriés
    feature_dict = {
        "Temperature (K)": features.temperature,
        "Luminosity(L/Lo)": features.luminosity,
        "Radius(R/Ro)": features.radius,
        "Absolute magnitude(Mv)": features.magnitude,
        "Star color": features.star_color,
        "Spectral Class": features.spectral_class
    }
    feature_df = pd.DataFrame([feature_dict])

    # Prédiction en utilisant le modèle
    prediction = model.predict(feature_df)
    
    # Convertir la prédiction en un type Python natif (par exemple int ou float)
    prediction = prediction[0].item() if isinstance(prediction[0], (np.generic, np.ndarray)) else prediction[0]
    
    return {"prediction": prediction}