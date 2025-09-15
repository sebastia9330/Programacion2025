import oracledb
import polars as pl
import pandas as pd  # puente temporal

# Conexión Oracle
conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)

# 1. Ejecuta tu consulta en Oracle
sql_movs = "SELECT * FROM copia_stg_fac_fiananciera"
sql_regras = "SELECT * FROM copia_tabla_parametros_2"

df_movs_pd = pd.read_sql(sql_movs, conn)
df_regras_pd = pd.read_sql(sql_regras, conn)

# 2. Convierte los DataFrames de pandas a polars
df_movs = pl.from_pandas(df_movs_pd)
df_regras = pl.from_pandas(df_regras_pd)

# 3. Ahora ya puedes trabajar en Polars normalmente
print(df_movs.shape)
print(df_regras.head())
