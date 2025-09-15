import polars as pl

df_mer = pl.DataFrame({
    "Producto": ["Pan","Leche","Queso","Jabón"],
    "Precio": [1500,3000,5000,2000],
    "Categoria": ["Alimentos", "Lácteos", "Lácteos", "Aseo"]
})


filtro = df_mer.filter(
    (pl.col("Precio") > 2000)
)
print("Filtrados (>2000 COP):")
print(filtro)


df_mer = df_mer.with_columns([
    (pl.col("Precio") / 4000).round(2).alias("precio_dólares")
])

ordenado = df_mer.sort("precio_dólares", descending=True)
print("\nOrdenados por precio_dólares (desc):")
print(ordenado)