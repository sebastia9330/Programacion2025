import oracledb
import pandas as pd

conn = oracledb.connect(
    user="usuario",
    password="contraseña",
    dsn="host:puerto/nombre del servicio"
)
print("Conexión exitosa!")

#objeto que lanza consultas y recibe resultados.
cursor = conn.cursor()

#primera consulta
sql = "SELECT * FROM STG_FAC_FINANCIERA WHERE ROWNUM <= 10"
cursor.execute(sql)

#recibir resultados uno por uno
"""for row in cursor:
    print(row)"""

#todos al tiempo
results = cursor.fetchall()
for row in results:
    print(row)

#DESCARGAR LA TABLA STG
df = pd.read_sql("SELECT * FROM STG_FAC_FINANCIERA", con = conn)

#Guardar resultado csv
df.to_csv("STG_FAC_financiera.csv", sep=";", index=False)



conn.close()


