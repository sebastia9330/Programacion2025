import pandas as pd


#importar archivo
df = pd.read_csv("inversiones.csv", encoding="ISO-8859-1", sep=";")
print(df)

#seleccionar las columnas que queremos cargar
df = pd.read_csv("inversiones.csv", encoding="ISO-8859-1", sep=";" , usecols=['KO', 'VALOR INV'])
print(df)

#traer datos de una web
df = pd.read_html('https://dolar.wilkinsonpc.com.co/')[0]
print(df)

#exportar datos a csv
df.to_csv('datos.csv', index=False)
print(df)

#exportar solo columnas
df['Valor'].to_csv('datos.csv', index=False)
print(df)

#exportar a excel
df.to_excel('datos.xlsx', index=False)


