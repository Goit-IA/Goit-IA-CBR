import nltk
import string

nltk.download('punkt')

def preprocess_text(text):
    # Minúsculas
    text = text.lower()
    # Eliminamos puntuación
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenización
    tokens = nltk.word_tokenize(text)
    return tokens
