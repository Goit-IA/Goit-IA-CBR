import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches

nltk.download('punkt_tab')
nltk.download('stopwords')

def cargar_base_datos(archivo_csv):
    base_datos = {}
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            if len(fila) >= 2:
                pregunta, respuesta = fila
                base_datos[pregunta.lower()] = respuesta
    return base_datos

def procesar_texto(texto):
    palabras = word_tokenize(texto.lower())
    palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in stopwords.words('spanish')]
    return " ".join(palabras_filtradas)

def buscar_respuesta(base_datos, pregunta_usuario):
    pregunta_procesada = procesar_texto(pregunta_usuario)
    coincidencias = get_close_matches(pregunta_procesada, base_datos.keys(), n=1, cutoff=0.6)
    if coincidencias:
        return base_datos[coincidencias[0]]
    return "Lo siento, no tengo una respuesta para eso."

def main():
    archivo_csv = "base_datos.csv"  # Asegúrate de que el archivo existe
    base_datos = cargar_base_datos(archivo_csv)
    
    print("Chatbot: ¡Hola! Pregúntame algo. Escribe 'salir' para terminar.")
    while True:
        pregunta_usuario = input("Tú: ")
        if pregunta_usuario.lower() == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        respuesta = buscar_respuesta(base_datos, pregunta_usuario)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
