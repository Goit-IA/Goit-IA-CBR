# Importa la biblioteca pandas
import pandas as pd

# Lee el archivo CSV en un DataFrame
def leer_csv(ruta_archivo):
        # Intenta leer el archivo CSV
        df = pd.read_csv(ruta_archivo)
        
        # Muestra las primeras filas del DataFrame
        print(df.head())

# Ruta al archivo CSV que deseas leer
ruta_archivo = 'Bajas.csv'

# Llama a la función para leer y visualizar el archivo
leer_csv(ruta_archivo)


