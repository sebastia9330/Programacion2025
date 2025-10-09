import polars as pl
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource

# Activar visualización en notebook
output_notebook()

# Datos con Polars
df = pl.DataFrame({
    "x": range(10),
    "y": [v**2 for v in range(10)]
})

# Convertir a pandas para usar en Bokeh
source = ColumnDataSource(df.to_pandas())

# Crear gráfico
p = figure(title="Ejemplo Polars + Bokeh")
p.line(x="x", y="y", source=source, line_width=2)
p.scatter(x="x", y="y", source=source, size=8, color="red", marker="circle")

show(p)
