#Ejercicio 24
#Pide un número del 1 al 7 y muestra el día de la semana correspondiente (1=Lunes, ..., 7=Domingo).


try:
    numDia = int(input("Digita un numero entre 1 al 7 para saber a que dia corresponde: "))

    if(numDia == 1):
        print(f"El número {numDia} corresponde al dia Lunes")
    elif(numDia == 2):
        print(f"El número {numDia} corresponde al dia Martes")
    elif(numDia == 3):
        print(f"El número {numDia} corresponde al dia Miercoles")
    elif(numDia == 4):
        print(f"El número {numDia} corresponde al dia Jueves")
    elif(numDia == 5):
        print(f"El número {numDia} corresponde al dia Viernes")
    elif(numDia == 6):
        print(f"El número {numDia} corresponde al dia Sabado")
    elif(numDia == 7):
        print(f"El número {numDia} corresponde al dia Domingo")
    else:
        print("Error el numero es mayor a 7")
except ValueError:
    print("Número digitado no valido")