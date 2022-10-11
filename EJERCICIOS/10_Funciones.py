
def saludarEstudiante(nombre):  #DEfinicion de la funcion
    saludo = "hola" + " " + nombre
    print(saludo) #Esto no es un return, simplemente es una impresion en pantalla

saludoRecibido = saludarEstudiante("Cristian Pachon")
print(saludoRecibido)

a = print("hoolaMundoCruel")
print("-----", a)

"""
1) Desarrollar una funcion que reciba dos numeros y
devuelva la suma de ambos

2) Desarrollar una funcion que reciba dos listas y
devuelva una nueva lista, que sume elemento a elemento

3) Desarrollar una funcion que no reciba parametros
   y que no retorne valores, pero que sirva para 
   imprimir un mensaje de 3 lineas

4) Desarrollar una funcion, que reciba un diccionario
   de calificaciones (nombre-calificacion)
   y retorne el promedio
"""

def sumarNumeros(numero1, numero2): #Definir funcion
    suma = numero1 + numero2
    return suma
suma1 = sumarNumeros(2,3)  # Invocar o llamar la funcion
print("suma1", suma1)
suma2 = sumarNumeros(numero2 = 3, numero1 = 2)  # Invocar o llamar la funcion
print("suma1", suma2)

def sumaDeListas(lista1, lista2): #Definir funcion y sus parametros de entrada
    tamañoLista = len(lista1)
    listaResultante = []
    for indice in range(0, tamañoLista):
        suma = lista1[indice] + lista2[indice]
        listaResultante.append(suma)
    return listaResultante        #Salida de la funcion

listaSumada = sumaDeListas([1,2,3], [1,1,1])  #Invocacion de la funcion
print(listaSumada)



