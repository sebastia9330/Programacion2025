import oracledb
import pandas as pd
import polars as pl
import os

# Rutas a los archivos CSV
ruta_csv_mov = "prueba5.csv"
ruta_csv_reg = "reg_prueba5.csv"

try:
    print("Intentando conexión a Oracle...")
    conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)

    print("✅ Conexión exitosa a Oracle")

    # Consultas desde Oracle
    df_mov = pd.read_sql("""
        SELECT NUM_ID_CIA, STR_ID_CENTRO_COSTO, STR_CUENTA_AUXILIAR, NUM_LINEA_ID_MOVTO
        FROM STG_FAC_FINANCIERA
    """, conn)

    df_reg = pd.read_sql("""
        SELECT NUM_ID_CIA, STR_NOMBRE_CONCEPTO, STR_NOMBRE_GRUPO,
                STR_ID_CCOSTO_AUXILIAR, STR_CUENTA, STR_CONDICION
        FROM TABLA_PARAMETROS
    """, conn)

    # Convertir a LazyFrames
    lz_mov = pl.from_pandas(df_mov).lazy()
    lz_reg = pl.from_pandas(df_reg).lazy()

    # Guardar CSV para futuros usos sin conexión
    lz_mov.collect().write_csv(ruta_csv_mov, separator=";")
    lz_reg.collect().write_csv(ruta_csv_reg, separator=";")

    print("✅ Datos cargados desde Oracle y exportados a CSV")

except Exception as e:
    print(f"⚠️ No se pudo conectar a Oracle: {e}")
    print("📁 Cargando datos desde archivos CSV locales...")

    if os.path.exists(ruta_csv_mov) and os.path.exists(ruta_csv_reg):
        lz_mov = pl.read_csv(
            ruta_csv_mov,
            separator=";",
            schema_overrides={
                "NUM_ID_CIA": pl.Int64,
                "STR_ID_CENTRO_COSTO": pl.Utf8,
                "STR_CUENTA_AUXILIAR": pl.Utf8,
                "NUM_LINEA_ID_MOVTO": pl.Int64
            }
        ).lazy()

        lz_reg = pl.read_csv(
            ruta_csv_reg,
            separator=";",
            schema_overrides={
                "NUM_ID_CIA": pl.Int64,
                "STR_NOMBRE_CONCEPTO": pl.Utf8,
                "STR_NOMBRE_GRUPO": pl.Utf8,
                "STR_ID_CCOSTO_AUXILIAR": pl.Utf8,
                "STR_CUENTA": pl.Utf8,
                "STR_CONDICION": pl.Utf8
            }
        ).lazy()
        print("✅ Datos cargados desde CSV con esquema definido")
    else:
        raise FileNotFoundError("❌ No se pudo conectar a Oracle y no existen los archivos CSV locales.")

print("dejamos solo las reglas que se usan con los movimientos que tenemos")
cias_mov = lz_mov.select(pl.col("NUM_ID_CIA").unique()).collect()["NUM_ID_CIA"].to_list()
cias_reg = lz_reg.select(pl.col("NUM_ID_CIA").unique()).collect()["NUM_ID_CIA"].to_list()
lz_filtrado = lz_reg.filter(pl.col("NUM_ID_CIA").is_in(cias_mov))

print("dividimos la el lazyframe lz_filtrado en prefijo y exacta por su cuenta")
lz_filtrado = lz_filtrado.with_columns([
    pl.col("STR_CUENTA").str.len_chars().alias("LARGO_CUENTA"),
    (pl.col("STR_CUENTA").str.len_chars() < 7).alias("ES_PREFIJO")
])
lz_reglas_exactas = lz_filtrado.filter(pl.col("ES_PREFIJO") == False)
lz_reglas_prefijo = lz_filtrado.filter(pl.col("ES_PREFIJO") == True) 

lz_join_exactas = lz_mov.join(
    lz_reglas_exactas,
    left_on=["NUM_ID_CIA", "STR_ID_CENTRO_COSTO", "STR_CUENTA_AUXILIAR"],
    right_on=["NUM_ID_CIA", "STR_ID_CCOSTO_AUXILIAR", "STR_CUENTA"],
    how="inner"
)

print(lz_join_exactas.select([
    "NUM_ID_CIA",
    "STR_ID_CENTRO_COSTO",
    "STR_CUENTA_AUXILIAR",
    "STR_NOMBRE_CONCEPTO",
    "STR_NOMBRE_GRUPO"
]).limit(5).collect())