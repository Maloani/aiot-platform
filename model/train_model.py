import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Génération de données synthétiques
np.random.seed(42)
n_samples = 5000
traffic_min, traffic_max = 0, 2000
traffic = np.random.uniform(traffic_min, traffic_max, n_samples).reshape(-1, 1)

midpoint = 1000
steepness = 0.008
prob = 1 / (1 + np.exp(-steepness * (traffic - midpoint)))
labels = np.random.binomial(1, prob.flatten())

# Création et entraînement du pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(C=1.0, random_state=42))
])
pipeline.fit(traffic, labels)

# Sauvegarde dans le dossier model/
model_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(model_dir, 'model.pkl')
joblib.dump(pipeline, model_path)
print(f"✅ Modèle sauvegardé dans {model_path}")