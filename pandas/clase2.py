import pandas as pd
import numpy as np

datos = {
    "Nombre": ['Dilza', 'Sebastian', 'Doris', 'Samuel'],
    "Edad": [30,32,11,46]
}

df = pd.DataFrame(datos)
print(df)

numeros = np.array([[1,2,3], [4,5,6]])

df1 = pd.DataFrame(numeros)
print(df1)

df2 = pd.read_csv("inversiones.csv", encoding="ISO-8859-1", sep=";")
print(df2.columns)

print(df2["VALOR INV"])

columnasNumericas = df2.select_dtypes(include='bool')
print(columnasNumericas)

df2["inversionista"] = "Samuel"
print(df2)

df2 = df2.drop("inversionista", axis=1)
print(df2)

primerasCol = df2.iloc[:, :3]
print(primerasCol)


inicial = df2.loc[:, df2.columns.str.startswith('7')]

print(inicial)