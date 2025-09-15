import pandas as pd

# Cargar el archivo CSV original
#archivo = "datos.csv"  # Asegúrate que esta ruta es correcta
df = pd.read_csv("filtro.csv", sep=';', dtype={"cuenta": "Int64", "INICIO": "Int64", "FIN": "Int64"})

#print("Original:")
#print(df.head())

# Procesar centros a incluir
incluye = df[['cia', 'cuenta', 'id','NOMBRE', 'nombre', 'INCLUYE_CC' ,'INICIO', 'FIN']].copy()
incluye['INCLUYE_CC'] = incluye['INCLUYE_CC'].fillna('')
incluye = incluye[incluye['INCLUYE_CC'] != '']
incluye['INCLUYE_CC'] = incluye['INCLUYE_CC'].astype(str).str.split(',')
incluye = incluye.explode('INCLUYE_CC')
incluye['centro_costo'] = incluye['INCLUYE_CC'].str.strip()
incluye['comportamiento'] = 'incluir'
incluye = incluye[['cia','cuenta', 'id','NOMBRE', 'nombre','centro_costo', 'comportamiento','INICIO', 'FIN']]
incluye = incluye.rename(columns={'NOMBRE': 'tipo_de_gasto'})


# Procesar centros a excluir
excluye = df[['cia','cuenta', 'id','NOMBRE', 'nombre','EXCLUYE_CC' ,'INICIO', 'FIN']].copy()
excluye['EXCLUYE_CC'] = excluye['EXCLUYE_CC'].fillna('')
excluye = excluye[excluye['EXCLUYE_CC'] != '']
excluye['EXCLUYE_CC'] = excluye['EXCLUYE_CC'].astype(str).str.split(',')
excluye = excluye.explode('EXCLUYE_CC')
excluye['centro_costo'] = excluye['EXCLUYE_CC'].str.strip()
excluye['comportamiento'] = 'excluir'
excluye = excluye[['cia','cuenta', 'id','NOMBRE', 'nombre','centro_costo', 'comportamiento','INICIO', 'FIN']]
excluye = excluye.rename(columns={'NOMBRE': 'tipo_de_gasto'})

# Unir ambos DataFrames
resultado = pd.concat([incluye, excluye], ignore_index=True)

# Mostrar el resultado
#print("\nResultado final:")
#print(resultado.head())

# Guardar a un nuevo CSV
resultado.to_csv("resultado_cc_expandido.csv", sep=";" ,index=False)
