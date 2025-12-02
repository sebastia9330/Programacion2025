import pandas as pd

datos = {'nombre': ['Sebastian Carrero', 'Dilza Robles', 'Samuel Carrero', 'Doris Ortiz'],
        'edad': [32,30,11,50],
        'ciudad': ['Bogota', 'Tunja', 'Leticia', 'Bucaramanga']}

df = pd.DataFrame(datos)
print(df)

#separar una columnma
df[['nombre', 'apellido']] = df['nombre'].str.split(' ', expand=True)
print(df)


df['edad'] = df['edad'].apply(lambda x: x +5)
print(df)

def convertirMayusculas(x):
    return x.upper()


df['nombre'] = df['nombre'].apply(convertirMayusculas)
print(df)

#funcion promedio
promedioEdad = df['edad'].mean()
print(promedioEdad)

#funcion suma
sumaedad = df['edad'].sum()
print(sumaedad)

#funcion maximo
maximoedad = df['edad'].max()
print(maximoedad)


#funcion minimo
minimoEdad = df['edad'].min()
print(minimoEdad)

#Remplazar nombres
df['nombre'] = df['nombre'].replace("SAMUEL CARRERO", "Samuel Felipe Carrero")
print(df)


#REMPLAZAR POR UNA INICIAL
df['nombre'] = df['nombre'].replace(r"^S.*", "Anonimo", regex=True)
print(df)

#separar texto
df['nombre'] = df['nombre'].str.split('')
print(df)
