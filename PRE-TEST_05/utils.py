def print_options(options):
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def get_user_selection(options):
    while True:
        try:
            choice = int(input("Selecciona una opción: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Por favor selecciona un número válido.")
        except ValueError:
            print("Por favor ingresa un número.")
