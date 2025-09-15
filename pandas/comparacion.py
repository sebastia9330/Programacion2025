import pandas as pd

# Leer los dos archivos
df_incluir = pd.read_csv('movimientos_incluir.csv', sep=";")
df_excluir = pd.read_csv('movimientos_excluir.csv', sep=";")

# Definir las columnas que vamos a comparar
cols_comparacion = [
    'NUM_ID_CIA',
    'STR_ID_CENTRO_COSTO',
    'STR_CUENTA_AUXILIAR',
    'NUM_PERIODO_FECHA',
    'NUM_LINEA_ID_MOVTO',
    'STR_NOMBRE_CONCEPTO',
    'STR_NOMBRE_GRUPO'
]

# Hacer un inner merge para encontrar registros idénticos
df_iguales = pd.merge(
    df_incluir[cols_comparacion],
    df_excluir[cols_comparacion],
    on=cols_comparacion,
    how='inner'
)

print(f"Registros idénticos encontrados: {len(df_iguales)}")
print(df_iguales.head())

# Exportar resultado si quieres
df_iguales.to_csv('movimientos_iguales_incluir_excluir.csv', sep=";" ,index=False)
