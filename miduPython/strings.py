##### Strings #####


myString = "Hola"
myOtherString = "hola2"

print(len(myString))
print(len(myOtherString))

print(myString + " " + myOtherString)

myNewLineString = "Esto es un string \ncon salto de linea"
print(myNewLineString)

myTabString = "\tEste es un string con tabulacion"
print(myTabString)

myScapeString = "\tEste es un string \nEscapado"
print(myScapeString)

##### Formateo #####
nombre = "Sebastián"
apellido = "Carrero"
edad = 30

print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")
print("Mi nombre es {} {} y mi edad es {}".format(nombre,apellido,edad))
print("Mi nombre es %s %s y mi edad es %s" %(nombre,apellido,edad))

##### Desempaquetado de Caracteres #####
lenguaje = "python"
a,b,c,d,e,f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

##### Division de Strings #####
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-1]
print(lenguaje_slice)

##### Reverso #####
reverso_lenguaje = lenguaje[::-1]
print(reverso_lenguaje)

##### Salto #####
salto_lenguaje = lenguaje[0:6:2]
print(salto_lenguaje)

##### Funciones #####
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.isupper())
print(lenguaje.startswith("py"))