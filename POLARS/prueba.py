import oracledb
import pandas as pd

# Conexión
conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)


# Leer tablas
query_movs = """
SELECT NUM_ID_CIA, STR_ID_CENTRO_COSTO, STR_CUENTA_AUXILIAR,
    NUM_PERIODO_FECHA, NUM_LINEA_ID_MOVTO
FROM STG_FAC_FINANCIERA
"""
df_movs = pd.read_sql(query_movs, conn)

query_reglas = """
SELECT NUM_ID_CIA, STR_NOMBRE_CONCEPTO, STR_NOMBRE_GRUPO,
    STR_ID_CCOSTO_AUXILIAR, STR_CUENTA,
    STR_CONDICION, NUM_INICIO, NUM_FIN
FROM TABLA_PARAMETROS_2
"""
df_reglas = pd.read_sql(query_reglas, conn)

# Limpiar espacios
for col in ['STR_CUENTA_AUXILIAR', 'STR_ID_CENTRO_COSTO']:
    df_movs[col] = df_movs[col].str.strip()

for col in ['STR_CUENTA', 'STR_ID_CCOSTO_AUXILIAR']:
    df_reglas[col] = df_reglas[col].str.strip()

# Merge por CIA y Centro de Costo
merged = df_movs.merge(
    df_reglas,
    left_on=['NUM_ID_CIA', 'STR_ID_CENTRO_COSTO'],
    right_on=['NUM_ID_CIA', 'STR_ID_CCOSTO_AUXILIAR'],
    how='left'
)

# Filtrar por periodo válido de la regla
merged = merged[
    (merged['NUM_PERIODO_FECHA'] >= merged['NUM_INICIO']) &
    (merged['NUM_PERIODO_FECHA'] <= merged['NUM_FIN'])
]

# Verificar match exacto o por prefijo
def match_cuenta(row):
    mov_cuenta = str(row['STR_CUENTA_AUXILIAR'])
    regla_cuenta = str(row['STR_CUENTA'])
    if pd.isnull(regla_cuenta) or pd.isnull(mov_cuenta):
        return False
    if mov_cuenta == regla_cuenta:
        return True
    if mov_cuenta.startswith(regla_cuenta):
        return True
    return False

merged['CUENTA_MATCH'] = merged.apply(match_cuenta, axis=1)

# Mantener solo los movimientos con cuenta match
reglas_aplicadas = merged[merged['CUENTA_MATCH']].copy()

# Asignar código de condición 1/0
reglas_aplicadas['CODIGO_REGLA'] = reglas_aplicadas['STR_CONDICION'].map({
    'incluir': 1,
    'excluir': 0
}).fillna(2).astype(int)

# Movimientos con match + código
resultados_con_match = df_movs.merge(
    reglas_aplicadas[[
        'NUM_LINEA_ID_MOVTO',
        'CODIGO_REGLA',
        'STR_NOMBRE_CONCEPTO',
        'STR_NOMBRE_GRUPO'
    ]],
    on='NUM_LINEA_ID_MOVTO',
    how='left'
)

# Asignar 2 a los movimientos que no tuvieron ningún match (NaN en CODIGO_REGLA)
resultados_con_match['CODIGO_REGLA'] = resultados_con_match['CODIGO_REGLA'].fillna(2).astype(int)

# Resultado final con todo
resultados_final = resultados_con_match[[
    'NUM_LINEA_ID_MOVTO',
    'NUM_ID_CIA',
    'STR_ID_CENTRO_COSTO',
    'STR_CUENTA_AUXILIAR',
    'NUM_PERIODO_FECHA',
    'CODIGO_REGLA',
    'STR_NOMBRE_CONCEPTO',
    'STR_NOMBRE_GRUPO'
]]

# Guardar en CSV
resultados_final.to_csv('movimientos_todos_con_codigo.csv', sep=";" ,index=False)
print(resultados_final.head())


print("Conexión exitosa!")