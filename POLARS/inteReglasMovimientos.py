import oracledb
import pandas as pd
import polars as pl

# 1️⃣ Conexión a Oracle
print("✅ Conectando a Oracle...")
conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)

# 2️⃣ Cargar datos
print("✅ Cargando movimientos...")
df_mov = pd.read_sql("""
    SELECT NUM_ID_CIA, STR_ID_CENTRO_COSTO, STR_CUENTA_AUXILIAR,
            NUM_PERIODO_FECHA, NUM_LINEA_ID_MOVTO
    FROM STG_FAC_FINANCIERA
""", conn)

print("✅ Cargando reglas...")
df_reglas = pd.read_sql("""
    SELECT NUM_ID_CIA, STR_NOMBRE_CONCEPTO, STR_NOMBRE_GRUPO,
            STR_ID_CCOSTO_AUXILIAR, STR_CUENTA, NUM_INICIO, NUM_FIN, STR_CONDICION
    FROM TABLA_PARAMETROS
""", conn)

# 3️⃣ Convertir a Polars LazyFrames
print("✅ Convirtiendo a Polars LazyFrames...")
lf_mov = pl.from_pandas(df_mov).lazy()


lf_reglas = pl.from_pandas(df_reglas).lazy().with_columns([
    pl.col("NUM_INICIO").fill_null(0).cast(pl.Int64),
    pl.col("NUM_FIN").fill_null(999999).cast(pl.Int64),
    pl.col("STR_CUENTA").str.len_chars().alias("LARGO_CUENTA"),
    (pl.col("STR_CUENTA").str.len_chars() < 7).alias("ES_PREFIJO")
])

print("✅ Movimientos y Reglas cargados en LazyFrames")

# 4️⃣ Filtrar reglas por compañías presentes
print("\n✅ Filtrando compañías únicas en movimientos")
cias_list = lf_mov.select("NUM_ID_CIA").unique().collect()["NUM_ID_CIA"].to_list()
print(f"✅ Compañías encontradas: {len(cias_list)}")

lf_reglas = lf_reglas.filter(pl.col("NUM_ID_CIA").is_in(cias_list))
print("✅ Filtro de reglas por compañías aplicado")

# 5️⃣ Procesar por compañía
print("\n✅ Procesando por compañía en bucle optimizado")
resultados = []

for cia in cias_list:
    print(f"\n🔄 Procesando compañía: {cia}")

    mov_cia = lf_mov.filter(pl.col("NUM_ID_CIA") == cia)
    reglas_cia = lf_reglas.filter(pl.col("NUM_ID_CIA") == cia)

    # 🚀 OPTIMIZACIÓN: aplicar filtros importantes ANTES del collect
    pipeline = (
        mov_cia
        .join(reglas_cia, on="NUM_ID_CIA", how="inner")
        .filter(
            (pl.col("NUM_PERIODO_FECHA") >= pl.col("NUM_INICIO")) &
            (pl.col("NUM_PERIODO_FECHA") <= pl.col("NUM_FIN"))
        )
        .filter(
            (pl.col("ES_PREFIJO") & pl.col("STR_CUENTA_AUXILIAR").str.starts_with(pl.col("STR_CUENTA"))) |
            (~pl.col("ES_PREFIJO") & (pl.col("STR_CUENTA_AUXILIAR") == pl.col("STR_CUENTA")))
        )
    )

    try:
        df_joined = pipeline.collect(streaming=True)
    except Exception as e:
        print(f"❌ Error en compañía {cia}: {e}")
        continue

    if df_joined.is_empty():
        print(f"⚠️ Sin resultados para compañía {cia}")
        continue

    # ✅ Paso 1: CCOSTO_MATCH
    df_joined = df_joined.lazy().with_columns([
        (pl.col("STR_ID_CENTRO_COSTO") == pl.col("STR_ID_CCOSTO_AUXILIAR")).alias("CCOSTO_MATCH")
    ]).collect(streaming=True)

    # ✅ Paso 2: CLASIFICACION
    df_joined = df_joined.lazy().with_columns([
        pl.when((pl.col("STR_CONDICION") == "incluir") & pl.col("CCOSTO_MATCH"))
        .then(pl.lit("clasificar"))
        .when((pl.col("STR_CONDICION") == "excluir") & pl.col("CCOSTO_MATCH"))
        .then(pl.lit("no_clasificar"))
        .otherwise(pl.lit("evaluar_reglas_exclusion"))
        .alias("CLASIFICACION")
    ]).collect(streaming=True)

    # ✅ Paso 3: TIENE_REGLA_EXCLUSION
    df_joined = df_joined.lazy().with_columns([
        pl.when((pl.col("STR_CONDICION") == "excluir") & pl.col("STR_ID_CCOSTO_AUXILIAR").is_not_null())
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("TIENE_REGLA_EXCLUSION")
    ]).collect(streaming=True)

    # ✅ Paso 4: CLASIFICACION_FINAL
    df_joined = df_joined.lazy().with_columns([
        pl.when(pl.col("CLASIFICACION").is_in(["clasificar", "no_clasificar"]))
        .then(pl.col("CLASIFICACION"))
        .when(pl.col("TIENE_REGLA_EXCLUSION"))
        .then(pl.lit("clasificar_por_exclusion"))
        .otherwise(pl.lit("clasificacion_por_prioridad"))
        .alias("CLASIFICACION_FINAL")
    ]).collect(streaming=True)

    # Resultado intermedio
    df_resultado = df_joined.select([
        "NUM_LINEA_ID_MOVTO",
        "NUM_ID_CIA",
        "STR_CUENTA_AUXILIAR",
        "STR_ID_CENTRO_COSTO",
        "STR_NOMBRE_CONCEPTO",
        "STR_NOMBRE_GRUPO",
        "CLASIFICACION_FINAL",
        "STR_CONDICION"
    ])

    resultados.append(df_resultado)
    print(f"✅ Compañía {cia} clasificada: {df_resultado.shape[0]} registros")


# 6️⃣ Concatenar y aplicar prioridad
if resultados:
    print("\n✅ Concatenando resultados finales...")
    df_final = pl.concat(resultados)

    # 🧠 Agregar prioridad numérica
    df_final = df_final.with_columns([
        pl.when(pl.col("CLASIFICACION_FINAL") == "clasificar").then(1)
        .when(pl.col("CLASIFICACION_FINAL") == "clasificar_por_exclusion").then(2)
        .when(pl.col("CLASIFICACION_FINAL") == "clasificacion_por_prioridad").then(3)
        .otherwise(4)
        .alias("PRIORIDAD")
    ])

    # 📌 Seleccionar solo la mejor clasificación por movimiento
    df_final = (
        df_final
        .sort(["NUM_LINEA_ID_MOVTO", "PRIORIDAD"])
        .unique(subset=["NUM_LINEA_ID_MOVTO"], keep="first")
        .drop("PRIORIDAD")
    )

    print(f"✅ Total clasificados únicos: {df_final.shape[0]}")
    print(df_final.head())

    df_final.write_csv("clasificacion_final.csv", separator=";")
    print(f"✅ Archivo exportado como clasificacion_final.csv")
else:
    print("⚠️ No hubo datos clasificados.")


print("✅ Reemplazando nulos")

df_pandas = df_final.to_pandas()



df_pandas = df_pandas.fillna('Nan')

cursor = conn.cursor()

print("✅ Ejecutando TRUNCATE TABLE ...")
cursor.execute("TRUNCATE TABLE MOVIMIENTOS_CLASIFICADOS")
print("✅ Tabla truncada")

sql_insert = """
    INSERT INTO MOVIMIENTOS_CLASIFICADOS(
        NUM_LINEA_ID_MOVTO,
        NUM_ID_CIA,
        STR_CUENTA_AUXILIAR,
        STR_ID_CENTRO_COSTO,
        STR_NOMBRE_CONCEPTO,
        STR_NOMBRE_GRUPO
    ) VALUES (:1, :2, :3, :4, :5, :6)
"""

data_to_insert = df_pandas[['NUM_LINEA_ID_MOVTO', 'NUM_ID_CIA', 'STR_CUENTA_AUXILIAR', 'STR_ID_CENTRO_COSTO', 'STR_NOMBRE_CONCEPTO', 'STR_NOMBRE_GRUPO' ]].values.tolist()

cursor.executemany(sql_insert, data_to_insert)
conn.commit()
cursor.close()

print("✅ Datos insertados en Oracle exitosamente")