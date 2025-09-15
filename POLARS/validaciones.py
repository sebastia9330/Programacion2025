import pandas as pd
import polars as pl
import oracledb

# ------------------------------------------
# 1️⃣ Conexión a Oracle
# ------------------------------------------
conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)

df_ls = pd.read_sql("SELECT NUM_ID_CIA,STR_ID_CENTRO_COSTO,NUM_LINEA_ID_MOVTO,STR_CUENTA_AUXILIAR FROM STG_FAC_FINANCIERA", conn)

df_ls = pl.from_pandas(df_ls)

df_ordenado2 = df_ls.sort("NUM_LINEA_ID_MOVTO")
#print(df_ordenado2)

df = pl.read_csv("clasificacion_final.csv", separator=";", infer_schema_length=0)

duplicados = df.filter(
    pl.col("NUM_LINEA_ID_MOVTO").is_in(
        df.group_by("NUM_LINEA_ID_MOVTO").count().filter(pl.col("count") > 1)["NUM_LINEA_ID_MOVTO"]
    )
)

ids_duplicados = (
    df.group_by("NUM_LINEA_ID_MOVTO").len().filter(pl.col("len") > 1).select("NUM_LINEA_ID_MOVTO")
)

print(ids_duplicados)
print(duplicados.head(5))

#Ordenar por num_linea
df_ordenado = df.sort("NUM_LINEA_ID_MOVTO")

print(df_ordenado.columns)
print(df_ordenado2.columns)

df_ordenado = df_ordenado.with_columns(
    pl.col('NUM_LINEA_ID_MOVTO').cast(pl.Utf8)
)

df_ordenado2 = df_ordenado2.with_columns(
    pl.col('NUM_LINEA_ID_MOVTO').cast(pl.Utf8)
)

faltantes = df_ordenado2.filter(
    ~pl.col('NUM_LINEA_ID_MOVTO').is_in(df_ordenado['NUM_LINEA_ID_MOVTO'].implode())
)

#guardar en archivo
faltantes.write_csv("ordenados.csv", separator=";")

