import polars as pl

# Cargar archivos
df_original = pl.read_csv("tabla_reglas_normalizada.csv", separator=";")
df_nuevo = pl.read_csv("tabla_reglas_normalizada2.csv", separator=";")

# Ordenar columnas alfabéticamente para comparar con estructura común
cols_ordenadas = sorted(set(df_original.columns) | set(df_nuevo.columns))
df_original = df_original.select([pl.col(c).cast(pl.Utf8).fill_null("").alias(c) if c in df_original.columns else pl.lit("").alias(c) for c in cols_ordenadas])
df_nuevo = df_nuevo.select([pl.col(c).cast(pl.Utf8).fill_null("").alias(c) if c in df_nuevo.columns else pl.lit("").alias(c) for c in cols_ordenadas])

# Crear versión string de la fila entera para comparar
df_original = df_original.with_columns(pl.concat_str(df_original.columns, separator="|").alias("row_str"))
df_nuevo = df_nuevo.with_columns(pl.concat_str(df_nuevo.columns, separator="|").alias("row_str"))

# Detectar filas eliminadas y nuevas
eliminadas = df_original.filter(~pl.col("row_str").is_in(df_nuevo["row_str"].implode()))
nuevas = df_nuevo.filter(~pl.col("row_str").is_in(df_original["row_str"].implode()))

# Mostrar diferencias
#print(f"🔻 Filas eliminadas ({eliminadas.shape[0]}):")
#print(eliminadas.select(cols_ordenadas))

print(f"\n🆕 Filas nuevas ({nuevas.shape[0]}):")
print(nuevas.select(cols_ordenadas))
