import polars as pl

#version de polars instalada
print(f"la version de polars es: {pl.__version__}")


# Crear un DataFrame simple
df = pl.DataFrame({
    "id": [101, 102, 103, 104],
    "nombre": ["Ana", "Luis", "Carlos", "Elena"],
    "edad": [28, 35, 42, 30],
    "ciudad": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
})

print(df)



#MODULO 1

#Explorar Datos
print(df.head()) #muestra las primeras 5 filas del dataframe
print(df.tail()) #muestra los ultimos registros del dataframe
print(df.describe()) #muestra algunos datos rapidos sobre el data fame como minimo maximo y promedio
print(df.columns) #muestra los nombres de las columnas
print(df.dtypes) #muestra el tipo de dato de cada columna


#seleccionar columnas
print(df.select("nombre")) #seleccionar una columna
print(df.select(["nombre", "edad"])) #seleccionar dos columnas o varias
print(df.select(pl.col("edad") * 5)) #operaciones con columnas


#filtar filas
print(df.filter(pl.col("edad") < 30)) #metodo filter para filtrar

#ordenar datos
print(df.sort("nombre", descending=False)) #metodo sort para organizar


#MODULO 2
# AGREGAR Y AGRUPAR
df.group_by("nombre").agg(
    pl.col("edad").mean().alias("edad_promedio")
)

print(df.group_by("nombre").agg(
    pl.col("edad").mean().alias("edad_promedio")
)) #crea una columna nueva con el promedio de la edad


#Joins entre DataFrames
df1 = pl.DataFrame({"id": [1,2], "valor": [100,200]})
df2 = pl.DataFrame({"id": [1,2], "cliente": ["Samuel", "Dilza"]})

print(df1.join(df2, on="id", how="inner"))


#Añadir columnas calculadas
df.with_columns([
    (pl.col("edad") * 2).alias("edad_doble")
])

df = df.with_columns([
    (pl.col("edad") * 2).alias("edad_doble")
])

#Condiciones tipo if-else
df = df.with_columns([
    pl.when(pl.col("edad") > 30)
        .then(pl.lit("Mayor"))
        .otherwise(pl.lit("Menor"))
        .alias("clasificacion")
])

print(df)

print(df.filter(
    (pl.col("edad") > 30) & (pl.col("ciudad") == "Cali")
))

df.select([
    pl.col("edad").sum(),
    pl.col("edad").mean(),
    pl.col("edad").max(),
    pl.col("edad").min()
])
