import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "A": [1,2,3,4,5],
    "B": [2,3,4,5,6],
    "C": [1,2,3,2,1]
})

print(df)
print()
print(df.describe())

print(f"Promedio: {df.mean()}")
print(f"Mediana: {df.median()}")
print(f"Moda: {df.mode()}")
print(f"Desviacion estandar: {df.std()}")
print(f"Varianza: {df.var()}")
print(f"Minimo: {df.min()}")
print(f"Maximo: {df.max()}")
print(f"Quintil: {df.quantile(0.25)}")
print(f"Valores unicos: {df["C"].nunique()}")
print(f"cuantos valores hay de cada registro dentro de la columna: {df['C'].value_counts()}")
print(f"Correlacion entre columnas A y B {df['A'].corr(df['B'])}")

#Grafico de calor por correlacion
correlacionMatrix = df.corr()
sn.heatmap(correlacionMatrix, annot=True)
plt.show()

#Grafico de lineas
df["C"].plot.line()
plt.show()

#Grafica de histograma
df["C"].plot.hist()
plt.show()

#Grafico de puntos con indicacion de columna
df.plot.scatter(x="A", y="C")
plt.show()

#Grafico de caja
df.plot.box()
plt.show()

#Grafico de area
df.plot.area()
plt.show()

#Grafico de torta
df["A"].plot.pie()
plt.show()

#Grafico de linea con indicaciones
df['A'].plot.line(color='red', title='Line Plot', xlabel='Index', ylabel='Valor')
plt.show()