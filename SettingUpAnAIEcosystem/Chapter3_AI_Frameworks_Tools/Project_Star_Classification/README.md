# TP3 - Classification of Star Type using MLflow, Streamlit, FastAPI, and Docker-compose

## Project Description

The goal of this project is to develop multiple models capable of classifying the type of a star based on several of its characteristics. The project uses Streamlit for the frontend, FastAPI for the backend, MLflow for model management, and Docker-compose for project deployment orchestration.

## Dependency Installation

Dependencies are included in a `requirements.txt` file. This file contains the necessary dependencies for the application's proper functioning, such as mlflow, scikit-learn, numpy, pandas, fastapi, uvicorn, and streamlit.

## Usage

To ensure the project works correctly, you must first create your models using MLflow. Then, manually enter the `experiment_id` and `run_id` in the backend's "main.py" file. Once your models are created, you need to build your image and start it.

```bash
docker-compose up --build
```

### MLflow

We use MLflow for model management. A file named `model_t.py` is specifically designed to register the various models we will use (supervised learning algorithms), such as SVC, RandomForest, logistic regression, and DecisionTreeClassifier trained on a dataset found on Kaggle. A pipeline is registered for each model, including data preprocessing.

Note that our focus is on deployment and orchestration. The models are not optimized, and some are overfitting.

### FastAPI

FastAPI is the backbone of our backend, allowing us to make API requests and use models from the MLflow model registry. There is only one function for a "POST" API request, which will enable us to make predictions with multiple models.

### Streamlit

Streamlit serves as our frontend. This is where the user will input data to classify their star and receive the star's class according to different models. It also contains a brief project description.

### Docker

We use Docker for deployment. We have two Dockerfiles, thus two containers, one for the backend and one for the frontend. Additionally, we have a `docker-compose.yml` file, which will handle orchestration during deployment. In our case, we ensure that FastAPI is operational before starting Streamlit.
