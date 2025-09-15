import oracledb
import pandas as pd
import polars as pl

#=================================================================================================================
# 1️⃣ Conexión y carga de datos
conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)


sql_nuevos_movs = """
    SELECT mov.NUM_ID_CIA,
        mov.STR_ID_CENTRO_COSTO,
        mov.STR_CUENTA_AUXILIAR,
        mov.NUM_PERIODO_FECHA,
        mov.NUM_LINEA_ID_MOVTO
    FROM STG_FAC_FINANCIERA mov
    WHERE NOT EXISTS(
        SELECT 1
        FROM MOVIMIENTOS_CLASIFICADOS clas
        WHERE clas.NUM_LINEA_ID_MOVTO = mov.NUM_LINEA_ID_MOVTO
    )    
"""
df_mov = pd.read_sql(sql_nuevos_movs, conn)

df_reglas = pd.read_sql("""
    SELECT NUM_ID_CIA, STR_NOMBRE_CONCEPTO, STR_NOMBRE_GRUPO,
            STR_ID_CCOSTO_AUXILIAR, STR_CUENTA, NUM_INICIO, NUM_FIN, STR_CONDICION
    FROM TABLA_PARAMETROS
""", conn)


if df_mov.empty:
    print("no hay movimientos nuevos")
else:
    print(f"Se encontraron {len(df_mov)} movimientos nuevos")
#=================================================================================================================

#=================================================================================================================
#conversion a polars
lf_mov = pl.from_pandas(df_mov).lazy()
lf_reglas = pl.from_pandas(df_reglas).lazy()
print("✅ Datos cargados en LazyFrames")
#=================================================================================================================

#=================================================================================================================
# ✅ Identificar compañías comunes
cias_mov = lf_mov.select(pl.col("NUM_ID_CIA").unique()).collect()["NUM_ID_CIA"].to_list()
cias_reglas = lf_reglas.select(pl.col("NUM_ID_CIA").unique()).collect()["NUM_ID_CIA"].to_list()
cias_comunes = sorted(list(set(cias_mov) & set(cias_reglas)))
print(f"✅ Compañías comunes encontradas: {cias_comunes}")
#=================================================================================================================

#=================================================================================================================
# ✅ Dividir reglas en exactas y por prefijo
lf_reglas = lf_reglas.with_columns([
    pl.col("STR_CUENTA").str.len_chars().alias("LARGO_CUENTA"),
    (pl.col("STR_CUENTA").str.len_chars() < 7).alias("ES_PREFIJO")
])
lf_reglas_exactas = lf_reglas.filter(pl.col("ES_PREFIJO") == False)
lf_reglas_prefijos = lf_reglas.filter(pl.col("ES_PREFIJO") == True)
print("✅ Reglas exactas y por prefijo separadas")
#=================================================================================================================

#=================================================================================================================
# ✅ Agrupar movimientos y reglas por compañía
bolsas_mov_por_cia = {}
reglas_exactas_por_cia = {}
movimientos_no_clasificados = {}

for cia in cias_comunes:
    movs_cia = lf_mov.filter(pl.col("NUM_ID_CIA") == cia)
    reglas_cia = lf_reglas_exactas.filter(pl.col("NUM_ID_CIA") == cia)

    bolsas_mov_por_cia[cia] = movs_cia
    reglas_exactas_por_cia[cia] = reglas_cia
    movimientos_no_clasificados[cia] = movs_cia
print(f"🔍 Preparada bolsas por compania")
#=================================================================================================================

