import polars as pl

#Agrupaciones + agg

df = pl.DataFrame({
    "ciudad": ["Bogotá", "Cali", "Bogotá", "Cali", "Medellín"],
    "ventas": [100, 200, 150, 250, 300]
})

""" df = df.group_by("ciudad").agg(
    pl.col("ventas").sum().alias("total_ventas")
)

print(df) """


#multiples agregaciones
df = df.group_by("ciudad").agg([
    pl.col("ventas").sum().alias("suma"),
    pl.col("ventas").mean().alias("promedio"),
    pl.col("ventas").max().alias("maximo")
])

print(df)

#unir varios dataframes

clietes = pl.DataFrame({
    "cliente_id": [1,2,3],
    "nombre": ["Samuel", "Sebastian", "Dilza"]
})

ventas = pl.DataFrame({
    "cliente_id": [1,2,1],
    "monto": [100,200,300]
})

df_i = clietes.join(ventas, on = "cliente_id", how = "inner")
df_l = clietes.join(ventas, on = "cliente_id", how = "left")
df_o = clietes.join(ventas, on = "cliente_id", how = "outer")
df_a = clietes.join(ventas, on = "cliente_id", how = "anti")

print(df_i)
print(df_l)
print(df_o)
print(df_a)


#Añadir columnas

df_w = pl.DataFrame({
    "nombre": ["Samuel", "Sebastian", "Dilza"],
    "edad": [20,35,42]
})

df_w = df_w.with_columns([
    (pl.col("edad") * 12).alias("edad_meses")
])

print(df_w)

#Condiciones (when-then-otherwise)

df_e = pl.DataFrame({
    "id": [101, 102, 103, 104],
    "nombre": ["Ana", "Luis", "Carlos", "Elena"],
    "edad": [28, 35, 42, 30],
    "ciudad": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
})


df_co = df_e.with_columns([
    pl.when(pl.col("edad") < 30)
    .then(pl.lit("Joven"))
    .when(pl.col("edad") < 40)
    .then(pl.lit("Adulto"))
    .otherwise(pl.lit("Mayor"))
    .alias("grupo_edad")
])

print(df_co)

#expresiones encadenadas y composicion
df_ex = (
    df_e.with_columns([
        (pl.col("edad") * 2).alias("edad_doble"),
        (pl.col("edad") + 5).alias("edad_mas_5")
    ])
    .filter(pl.col("edad") > 30)
    .sort("edad", descending=True)
)

print(df_ex)


#operacion entre columnas
df_ope = df_ex.with_columns([
    (pl.col("edad_doble") - pl.col("edad")).alias("diferencia")
])

print(df_ope)


#Ejercicio Basico clase2
productos = pl.DataFrame({
    "producto": ["Manzanas", "uvas", "mandarinas", "naranjas", "leche", "carne"],
    "categorias": ["frutas", "frutas", "frutas", "frutas", "lacteos", "carnicos"],
    "precio": [100, 150, 200, 250, 300, 350],
    "cantidad": [10, 20, 30, 40, 50, 60]
})

#agrupamiento
precio_categoria = productos.group_by("categorias").agg(
    pl.col("precio").sum().alias("total_categoria")
)

print(precio_categoria)

#Columna categoria
productos = productos.with_columns([
    pl.when(pl.col("precio") < 200)
    .then(pl.lit("Bajo"))
    .when(pl.col("precio") < 500)
    .then(pl.lit("Medio"))
    .otherwise(pl.lit("Alto"))
    .alias("nivel_precio")
])

productos = productos.sort("nivel_precio", descending=True)

print(productos)

