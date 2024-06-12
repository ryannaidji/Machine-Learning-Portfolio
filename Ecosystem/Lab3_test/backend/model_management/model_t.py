import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Chargement des données
data = pd.read_csv('../../data/stars_dataset.csv')

data.head()

# Prétraitement des couleurs d'étoiles
replacement_dict = {
    "Blue-white": "Blue White",
    "Blue white": "Blue White",
    "Blue-White": "Blue White",
    "yellow-white": "Yellowish White",
    "White-Yellow": "Yellowish White",
    "yellowish": "Yellowish",
    "white": "White",
    "Blue ": "Blue",
    "Blue white ": "Blue White",
    "Orange-Red": "Orange Red",
    "Pale yellow orange": "Pale Yellow Orange"
}
data["Star color"] = data["Star color"].replace(replacement_dict)

# Séparation des features et de la cible
X = data.drop('Star type', axis=1)
y = data['Star type']

# Préprocesseurs pour les données numériques et catégorielles
categorical_features = ["Spectral Class", "Star color"]
numeric_features = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)', 'Absolute magnitude(Mv)']

categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features)])

# Configuration MLflow
#mlflow.set_tracking_uri("file:///C:/Users/ryann/OneDrive/Desktop/AI/Mise en place d'un écosystème d'IA/Lab3_test/backend/mlruns")  # Changez le chemin selon votre configuration
mlflow.set_tracking_uri("../mlruns")
mlflow.set_experiment("Star_Type_Classification")

# Modèles à entraîner
models = {
    "Logistic_Regression": {"model": LogisticRegression(max_iter=1000), "test_size": 0.5},
    "Random_Forest": {"model": RandomForestClassifier(n_estimators=100), "test_size": 0.8},
    "Decision_Tree": {"model": DecisionTreeClassifier(), "test_size": 0.5},
    "SVC": {"model": SVC(kernel='linear'), "test_size": 0.2}
}

# Entraînement et évaluation des modèles
for name, model_info in models.items():
    with mlflow.start_run():
        # Division du dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=model_info['test_size'], random_state=42)

        # Création du pipeline complet
        pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model_info['model'])])

        # Entraînement du modèle
        pipeline.fit(X_train, y_train)
        
        # Prédiction et évaluation
        y_pred = pipeline.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Logging dans MLflow
        mlflow.log_params({"model": name, "max_iter": 1000 if name == 'Logistic_Regression' else None})
        mlflow.log_metrics({"accuracy": report['accuracy'], "weighted avg f1-score": report['weighted avg']['f1-score']})
        mlflow.sklearn.log_model(pipeline, "model")

        print(f"Results for {name}:")
        print(classification_report(y_test, y_pred))

# Fin de l'experimentation
mlflow.end_run()
