import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(1,10,size=(3,2)), columns=list('AB'))

df2 = pd.DataFrame(np.random.randint(1,10,size=(3,2)), columns=list('AB'))

print(df1)
print()
print(df2)
print()

#suma
dfSum = df1 + df2
print(dfSum)

#resta
dfRest = df1 - df2
print(dfRest)

#multiplicacion
dfMulti = df1 * df2
print(dfMulti)

#division
dfdivi = df1 / df2
print(dfdivi)

#operaciones aritmeticas con escalares
df1Plus2 = df1 + 2
print(df1Plus2)

#uso de funciones matematicas numpy
#raiz cuadrada
dfSqrt = np.sqrt(df1)
print(dfSqrt)
print()

df3 = pd.DataFrame(np.random.randint(1,10,size=(10,4)), columns=list('ABCD'))
print(df3)
print()

#Uso de funciones de agregacion
#sumar una columna
dfSumA = df3['A'].sum()
print(dfSumA)

#promedio de una columna
dfProme = df3['B'].mean()
print(dfProme)

#contar elementos de la columna
dfCount = df3['C'].count()
print(dfCount)

#uso de la funcion agg
dfAgg = df3.agg(['sum', 'mean', 'max', 'min', 'count'])
print(dfAgg)

df4 = pd.DataFrame({
    "A": ['perro','gato', 'perro','gato', 'perro','gato', 'perro','gato'],
    "B": ['uno', 'uno', 'dos', 'tres', 'dos','dos', 'uno', 'tres'],
    "C": np.random.randn(8),
    "D": np.random.randn(8)
})

print(df4)

#agrupacion por una columna mas suma
agrupacionSimple = df4.groupby('A').sum()
print(agrupacionSimple)

#agrupacion por varias columnas mas suma
agrupacionMultiple = df4.groupby(['A', 'B']).sum()
print(agrupacionMultiple)

#agrupacion por varias columnas mas promedio
agrupacionMultipleProme = df4.groupby(['A', 'B']).mean()
print(agrupacionMultipleProme)

#agrupacion por varias columnas mas varios metodos
agrupacionMultiple2 = df4.groupby(['A', 'B']).agg(['mean','sum'])
print(agrupacionMultiple2)

df5 = pd.DataFrame({
    "A":['A0', 'A1', 'A2', 'A3'],
    "B":['B0', 'B1', 'B2', 'B3'],
    "Key":['K0', 'K1', 'K2', 'K3']
})

df6 = pd.DataFrame({
    "C":['C0', 'C1', 'C2', 'C3', 'C4'],
    "D":['D0', 'D1', 'D2', 'D3','D4'],
    "Key":['K0', 'K1', 'K2', 'K3','K4']
})

print(df5)
print()
print(df6)

#concatenar data frames
dfConcat = pd.concat([df5, df6], axis=0)
print(dfConcat)

#fusionar con merge
#METODO OUTER
dfMerge = pd.merge(df5 , df6, on='Key', how='outer')
print(dfMerge)

#METODO INNER
dfMergeinner = pd.merge(df5 , df6, on='Key', how='inner')
print(dfMergeinner)

#METODO left
dfMergeleft = pd.merge(df5 , df6, on='Key', how='left')
print(dfMergeleft)

#METODO right
dfMergeright = pd.merge(df5 , df6, on='Key', how='right')
print(dfMergeright)

#metodo join
dfJoin = df5.join(df6, lsuffix='_df5', rsuffix='_df6')
print(dfJoin)