import pandas as pd

data = {
    'Nombre': ["sebastian", "Samuel", "Dilza", "Juan", "Doris", "Pedro", "Emma"],
    'Edad': [30,11,30,49,52,5,8],
    'Ciudad': ["Bogota", "Santa Marta", "Barranquilla", "Cali", "Cartagena", "Tunja", "Bucaramanga"]
}

df = pd.DataFrame(data)
print(df)

#Ordenar los datos de menor a mayor
dfo = df.sort_values(by="Edad")
print(dfo)

#Ordenar los datos de mayor a menor
dfa = df.sort_values(by="Edad", ascending=False)
print(dfa)

#ordenar por multiples columnas con indice reseteado y eliminado de columna
dfm = df.sort_values(by=["Ciudad","Edad"]).reset_index(drop=True)
print(dfm)

#Ordenar por indice
dfi = df.sort_index(ascending=False)
print(dfi)

#crear ranking de edades
df['Ranking de dades'] = df['Edad'].rank(method='first')
print(df)