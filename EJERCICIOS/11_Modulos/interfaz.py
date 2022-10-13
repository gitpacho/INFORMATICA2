"""
Este modulo se llama interfaz,
mediante el cual se imprime un separador,
un nombre, y unas variables de manera más
presentable utilizando funciones

tambien se almacena 1 variable
"""

cantidadDeFunciones = 3

def separador(caracter):
    sep = caracter * 50
    print(sep)

def imprimirNombre(nombre):
    saludo = "hola,mi nombre es interfaz y el tuyo " + nombre
    print(saludo)

def imprimirVariable(nombreVariable, variable):
    print(nombreVariable + " ====> " + variable)

