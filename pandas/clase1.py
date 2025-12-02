import pandas as pd

serie = pd.Series([1,2,3,4,5,6,7,8,9,100])

print(serie)

datos = {
    'Nombres': ['Ana', 'Carlos', 'Juan', 'Dilza', 'Samuel'],
    'Edad': [18,20,30,28,11]
}

df = pd.DataFrame(datos)
print(df)

df1 = pd.read_csv("inversiones.csv", encoding="ISO-8859-1", sep=";")
print(df1.shape)
print(df1.head())
dfOrdenadoKo = df1.sort_values('KO')
print(dfOrdenadoKo)
df1['KO'] = pd.to_numeric(df1['KO'], errors='coerce')

print(df1.columns)

dfFiltrado = df1[df1['KO'] > 60]
print(dfFiltrado)
