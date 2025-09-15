import pandas as pd

""" df_incluir = pd.read_csv('movimientos_incluir.csv')
df_excluir = pd.read_csv('movimientos_excluir.csv')

print("📄 Columnas de incluir:")
print(df_incluir.columns)

print("\n📄 Columnas de excluir:")
print(df_excluir.columns) """

df_menor =pd.read_csv("ordenados.csv",  sep=";")

df_menor = df_menor.sort_values("STR_CUENTA_AUXILIAR")
print(df_menor)

df_menor.to_csv("ordenados.csv", sep=";", index=False)
