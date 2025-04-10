from data_loader import get_unique_temas, get_unique_subtemas, get_unique_preguntas, get_respuesta
from utils import print_options, get_user_selection

def start_conversation(df):
    print("¡Hola! Bienvenido al chatbot. 😊")
    print("Por favor, selecciona el tema relacionado a tu pregunta:\n")

    while True:
        temas = get_unique_temas(df)
        print_options(temas)
        selected_tema = get_user_selection(temas)

        subtemas = get_unique_subtemas(df, selected_tema)
        print(f"\nPerfecto, selecciona un subtema relacionado con '{selected_tema}':\n")
        print_options(subtemas)
        selected_subtema = get_user_selection(subtemas)

        preguntas = get_unique_preguntas(df, selected_tema, selected_subtema)
        print(f"\nMuy bien, selecciona tu pregunta sobre '{selected_subtema}':\n")
        print_options(preguntas)
        selected_pregunta = get_user_selection(preguntas)

        respuesta = get_respuesta(df, selected_tema, selected_subtema, selected_pregunta)
        print(f"\nRespuesta: {respuesta}\n")

        otra = input("¿Tienes alguna otra pregunta? (escribe 'salir' para terminar): ").strip().lower()
        if otra == 'salir':
            print("¡Gracias por usar el chatbot! 👋")
            break
