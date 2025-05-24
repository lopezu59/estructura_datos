from nltk.tokenize import word_tokenize
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


# Palabras clave simples para cada prioridad
keywords = {
    'Alta': {'urgente', 'entregar', 'examen', 'hoy', 'deadline', 'importante', 'inmediato'},
    'Media': {'estudiar', 'leer', 'practicar', 'investigar', 'repasar', 'debo', 'planificar'},
    'Baja': {'cuando', 'algún', 'luego', 'si', 'eventualmente', 'nada','revisar', 'más tarde', 'después', 'más adelante'}
}

def classify_task(task):
    tokens = word_tokenize(task.lower())
    
    # Contar coincidencias por prioridad
    scores = {'Alta':0, 'Media':0, 'Baja':0}
    for token in tokens:
        for priority, keys in keywords.items():
            if token in keys:
                scores[priority] += 1

    # Si no hay coincidencias, baja prioridad por defecto
    if all(score == 0 for score in scores.values()):
        return 'Baja'

    # Retorna la prioridad con más coincidencias, priorizando Alta > Media > Baja en empate
    priorities_order = ['Alta', 'Media', 'Baja']
    return max(scores, key=lambda p: (scores[p], -priorities_order.index(p)))


