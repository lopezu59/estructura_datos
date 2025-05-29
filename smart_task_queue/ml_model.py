import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

# Rutas
CSV_PATH = 'data/tareas_prioridad.csv'
MODEL_PATH = 'modelo_prioridades.joblib'

# Entrenamiento del modelo
def entrenar_modelo():
    data = pd.read_csv(CSV_PATH)
    tareas = data['tarea']
    prioridades = data['prioridad']

    modelo = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])
    modelo.fit(tareas, prioridades)
    joblib.dump(modelo, MODEL_PATH)
    print("Modelo entrenado y guardado correctamente.")

# Clasificación de una nueva tarea
def clasificar_tarea(texto):
    if not os.path.exists(MODEL_PATH):
        entrenar_modelo()
    modelo = joblib.load(MODEL_PATH)
    return modelo.predict([texto])[0]

# Si ejecutas directamente este archivo, entrena
if __name__ == '__main__':
    entrenar_modelo()
