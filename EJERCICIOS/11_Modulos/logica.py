"""
Este modulo contiene 3 funciones de lógica para hacer 
lo siguiente:

* sumar 3 numeros
* sumar n numeros
* sumar 2 listas, elemento a elemento
"""

def sumar3Numeros(numero1, numero2, numero3): #entrada de la funcion
    resultado = numero1 + numero2 + numero3
    return resultado  #salida de la funcion

def sumarNumeros(*numeros):  #numeros se interpreta como lista
    #resultado = 0
    #for numero in numeros:
    #    resultado = resultado + numero
    resultado = sum(numeros)
    return resultado

def sumarListas(lista1, lista2):
    listaResultado = []
    for indice in range(0, len(lista1)):
        suma = lista1[indice] + lista2[indice]
        listaResultado.append(suma)
    return listaResultado





