import os
import sys
import joblib
import numpy as np
from flask import Flask, request, jsonify, send_from_directory

# Ajouter le chemin parent pour importer des modules si nécessaire
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__, static_folder='../dashboard', static_url_path='')

# Chemins
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model.pkl')
DASHBOARD_DIR = os.path.join(BASE_DIR, 'dashboard')

# Vérifier l'existence du modèle
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modèle introuvable : {MODEL_PATH}. Veuillez exécuter model/train_model.py")

# Charger le modèle
model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    """Sert l'interface utilisateur"""
    return send_from_directory(DASHBOARD_DIR, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint de prédiction.
    Attend : {"trafic": nombre}
    Retourne : {"prediction": 0 ou 1}
    """
    try:
        data = request.get_json()
        if not data or 'trafic' not in data:
            return jsonify({'error': 'Données manquantes'}), 400

        trafic_value = float(data['trafic'])
        input_array = np.array([[trafic_value]])
        prediction = model.predict(input_array)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5501)   # ou 8000, 8080, etc.