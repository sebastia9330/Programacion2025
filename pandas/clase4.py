import pandas as pd
import numpy as np


df = pd.DataFrame({'A':[2,10,12,16,17,18,19,200,np.nan,202],
                    'B':[2,10,12,16,17,18,19,200,np.nan,202],
                    'C':[2,10,12,16,17,18,19,200,np.nan,202]})

print(df)

print(df.isnull()) #imprimer true a los valores nulos
print(df.notnull()) #imprime false a los valores nulos
print(df.isnull().sum()) #cuenta los valores nulos dentro de las columnas

#eliminar las columnas con datos nulos
df_drop = df.dropna()
print(df_drop)

#eliminar columnas
df_drop_columns = df.dropna(axis=1)
print(df_drop_columns)

#llenado de valores faltantes con un valor constate
df_fill = df.fillna(value=0)
print(df_fill)

#lleanr el calor nulo con el valor de la fila anterior
df_fill_forward = df.fillna(method='ffill')
print(df_fill_forward)


#lleanr el calor nulo con el valor de la fila posterior
df_fill_backward = df.fillna(method='bfill')
print(df_fill_backward)

#llenar el dataframe con la media de los datos de la columna
df_fill_mean = df.fillna(df.mean())
print(df_fill_mean)

#lleando de datos faltantes usando interpolacion
df_fill_interpolate = df.interpolate()
print(df_fill_interpolate)