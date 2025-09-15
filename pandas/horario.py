import pandas as pd
from datetime import datetime, timedelta

# Lista de personas
personas = [
    "Laura Martínez", "Andrés Gómez", "Camila Rodríguez", "Juan Pablo Torres",
    "Daniela Sánchez", "Felipe Morales", "Valentina Herrera", "Sebastián López",
    "Natalia Castro", "Diego Ramírez", "Juliana Vargas", "Santiago Gutiérrez",
    "Mariana Ríos", "Cristian Pérez", "Andrea Torres", "Javier Álvarez",
    "Sofía Mendoza", "Carlos Patiño", "Paula Fernández", "Miguel Ángel Duarte",
    "Gabriela Ortiz", "Esteban Cárdenas", "Catalina Navarro", "Ricardo Salazar"
]

# Configuración
inicio_mañana = datetime.strptime("07:30", "%H:%M")
inicio_tarde = datetime.strptime("14:00", "%H:%M")
fin_dia = datetime.strptime("17:15", "%H:%M")
duracion_sesion = timedelta(minutes=60)  # duración de cada turno
correos_disponibles = 3

# Crear lista de turnos posibles (mañana y tarde)
turnos = []
hora_actual = inicio_mañana
while hora_actual + duracion_sesion <= datetime.strptime("13:00", "%H:%M"):
    turnos.append(hora_actual.strftime("%H:%M") + " - " + (hora_actual + duracion_sesion).strftime("%H:%M"))
    hora_actual += duracion_sesion

hora_actual = inicio_tarde
while hora_actual + duracion_sesion <= fin_dia:
    turnos.append(hora_actual.strftime("%H:%M") + " - " + (hora_actual + duracion_sesion).strftime("%H:%M"))
    hora_actual += duracion_sesion

# Asignar personas a turnos sin cruce (3 personas por turno)
horario = []
i = 0
for turno in turnos:
    for _ in range(correos_disponibles):
        if i < len(personas):
            horario.append({"Turno": turno, "Persona": personas[i]})
            i += 1

# Convertir a DataFrame
df_horario = pd.DataFrame(horario)
print(df_horario.head(30))