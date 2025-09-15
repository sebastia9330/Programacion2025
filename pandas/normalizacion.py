import pandas as pd

# Carga CSV
df = pd.read_csv("tabla_parametros.csv", sep=';', dtype={"cuenta": "string", "INICIO": "Int64", "FIN": "Int64"})

# Normalizador de listas
def expandir_listas(df, columna_lista, tipo_regla):
    df_filtrado = df[df[columna_lista].notnull()].copy()
    df_filtrado[columna_lista] = df_filtrado[columna_lista].str.replace(r'[\[\]]', '', regex=True)
    df_filtrado = df_filtrado.assign(
        ccosto=df_filtrado[columna_lista].str.split(',')
    ).explode('ccosto')
    df_filtrado['tipo'] = tipo_regla
    df_filtrado['ccosto'] = df_filtrado['ccosto'].str.strip()
    return df_filtrado[['cia', 'cuenta', 'NOMBRE', 'NOMBRE_G', 'ccosto', 'tipo', 'INICIO', 'FIN']]

# Normaliza las listas
incluye = expandir_listas(df, 'INCLUYE_CC', 'incluir')
excluye = expandir_listas(df, 'EXCLUYE_CC', 'excluir')

# Filtra las filas que no tienen ninguna lista → se aplican a toda la cuenta
sin_centros = df[df['INCLUYE_CC'].isnull() & df['EXCLUYE_CC'].isnull()].copy()
sin_centros['ccosto'] = None
sin_centros['tipo'] = 'incluir'  # o puedes dejarlo como 'ambos' o 'todos'
sin_centros = sin_centros[['cia', 'cuenta', 'NOMBRE', 'NOMBRE_G', 'ccosto', 'tipo', 'INICIO', 'FIN']]

# Unión final
df_normalizado = pd.concat([incluye, excluye, sin_centros], ignore_index=True)

# Exportar
df_normalizado.to_csv("tabla_reglas_normalizada.csv", sep=';', index=False)

# Vista previa
print(df_normalizado.head(10))
