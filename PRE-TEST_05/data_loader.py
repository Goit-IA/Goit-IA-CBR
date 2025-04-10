import pandas as pd

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

def get_unique_temas(df):
    return df['TEMA'].unique().tolist()

def get_unique_subtemas(df, tema):
    return df[df['TEMA'] == tema]['SUBTEMA'].unique().tolist()

def get_unique_preguntas(df, tema, subtema):
    return df[(df['TEMA'] == tema) & (df['SUBTEMA'] == subtema)]['PREGUNTA'].unique().tolist()

def get_respuesta(df, tema, subtema, pregunta):
    respuesta = df[
        (df['TEMA'] == tema) &
        (df['SUBTEMA'] == subtema) &
        (df['PREGUNTA'] == pregunta)
    ]['RESPUESTA']
    return respuesta.values[0] if not respuesta.empty else "No se encontró respuesta."
