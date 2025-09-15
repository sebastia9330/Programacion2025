import pandas as pd

# Cargar CSV
df = pd.read_csv("filtro.csv", sep=';', dtype={"cuenta": "Int64", "INICIO": "Int64", "FIN": "Int64"})

# Función para reemplazar saltos de línea por comas
def limpiar_centros(val):
    if pd.isnull(val):
        return val
    return str(val).replace('\n', '').replace('\r', '')

# Aplicar la función
df['INCLUYE_CC'] = df['INCLUYE_CC'].apply(limpiar_centros)
df['EXCLUYE_CC'] = df['EXCLUYE_CC'].apply(limpiar_centros)

# Guardar el archivo limpio
df.to_csv("tabla_parametros.csv", sep=';', index=False)

# Verifica
print(df[['INCLUYE_CC', 'EXCLUYE_CC']].head())
