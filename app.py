import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay
from sklearn.metrics import precision_score, recall_score

import flask
from flask import Flask, render_template, jsonify
import json
import requests

app = Flask(__name__)

#API_URL = 'http://127.0.0.1:5000'

def load_pickle(filename, path):
    with open(f'{path}/{filename}.pickle', 'rb') as f:
        return pickle.load(f)
    
data = load_pickle('creditcard', f'./')
model = load_pickle('rfc_model', f'./')

X_data = data.drop["Class"]
y_data = data["Class"]

@app.route('/predict/', methods=['GET'])
def model_predict():
# Prédictions
    y_pred = model.predict(X_data)
            
    # Métriques de performance
    accuracy = model.score(X_data, y_data).round(3)
    precision = precision_score(y_data, y_pred).round(3)
    recall = recall_score(y_data, y_pred).round(3)
    
    return jsonify({ 
      'accuracy': accuracy,
      'precision': precision,
      'recall': recall,
    })

if __name__ == "__main__":
    app.run(debug=True)