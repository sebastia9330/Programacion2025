def celsiusFahrenheit(valor):
    resultado = (valor * 1.8) + 32
    return resultado

def fahrenheitCelsius(valor):
    resultado = (valor - 32) * (5/9)
    return resultado

def centimetrosPulgadas(valor):
    resultado = valor /2.54
    return resultado

def pulgadaCentimetro(valor):
    resulltado = valor * 2.54
    return resulltado

def kiloLibra(valor):
    resultado = valor * 2.205
    return resultado

def libraKilo(valor):
    resulltado = valor / 2.205
    return resulltado


unidadInicial = input("Digita la unidad inicial: ").lower()
unidadFinal = input("Digita la unidad final: ").lower()
try:
    valor = float(input("Digita el valor inicial: "))

    if unidadInicial == "celsius" and unidadFinal == "fahrenheit":
        resultado = celsiusFahrenheit(valor)
        print(f"La temperatura {valor} grados Celsuis es igual a, {resultado} grados Fahrenheit")
    elif unidadInicial == "fahrenheit" and unidadFinal == "celsius":
        resultado = fahrenheitCelsius(valor)
        print(f"La temperatura {valor} grados Fahrenheit es igual a, {resultado} grados Celsius")
    elif unidadInicial == "centimetros" and unidadFinal == "pulgadas":
        resultado = centimetrosPulgadas(valor)
        print(f"La cantidad de {valor} centimetros es igual a {resultado} pulgadas")
    elif unidadInicial == "pulgadas" and unidadFinal == "centimetros":
        resultado = pulgadaCentimetro(valor)
        print(f"La cantidad de {valor} pulgadas es igual a {resultado} centimetros")
    elif unidadInicial == "kilos" and unidadFinal == "libras":
        resultado = kiloLibra(valor)
        print(f"La cantidad de {valor} Kilos es igual a {resultado} Libras")
    elif unidadInicial == "libras" and unidadFinal == "kilos":
        resultado = libraKilo(valor)
        print(f"La cantidad de {valor} libras es igual a {resultado:.2f} kilos")
    else:
        print("Unidades no válidas, intenta con celsius, fahrenheit, centimetros, pulgadas, kilogramos, libras")
except(ValueError):
    print("valor no valido, intenta de nuevo")


        


