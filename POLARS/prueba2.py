import polars as pl

#leer un archivo por los primeros 1000 registros
df = pl.read_csv("clasificacion_final.csv", separator=";" ,n_rows=1000, schema_overrides={"STR_CUENTA_AUXILIAR": pl.String})
df1 = pl.read_csv("STG_FAC_financiera.csv", separator=";", infer_schema_length=0)

#contar repetidos en una columna
conteo = df.group_by("NUM_LINEA_ID_MOVTO").count().filter(pl.col("count") > 1)

#muestra los registros de dos columnas seleccionadas
dosColum = df.select([pl.col(["NUM_ID_CIA","NUM_LINEA_ID_MOVTO"])]).head()
#print(dosColum)

#sumar dos columnas
suma = df1.select([pl.col(["num_credito", "num_debito"])]).sum()
print(suma)

#describe el conjunto de datos
describ = df.describe()

#print(describ)
#print(conteo)

#df.write_csv('movimientos_iguales_incluir_excluir.csv', separator=";")




