
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
   y retorne el promedio del curso

5) Desarrollar una funcion que reciba (como parametros de entrada) una cantidad
   indeterminada de numeros y retorne su producto
"""
######
def sumarNumeros(numero1, numero2): #Definir funcion
    suma = numero1 + numero2
    return suma
suma1 = sumarNumeros(2,3)  # Invocar o llamar la funcion
print("suma1", suma1)
suma2 = sumarNumeros(numero2 = 3, numero1 = 2)  # Invocar o llamar la funcion
print("suma1", suma2)

#######
def sumaDeListas(lista1, lista2): #Definir funcion y sus parametros de entrada
    tamañoLista = len(lista1)
    listaResultante = []
    for indice in range(0, tamañoLista):
        suma = lista1[indice] + lista2[indice]
        listaResultante.append(suma)
    return listaResultante        #Salida de la funcion

listaSumada = sumaDeListas([1,2,3], [1,1,1])  #Invocacion de la funcion
print(listaSumada)

########
def imprimirMensaje(): #Definir funcion sin parametros de entrada
    print("hola mundo")
    print("hola mundo cruel")
    print("hola mundo cruel python")  #No hay retorno

salida = imprimirMensaje() #no es necesario almacenar la salida en una variable, ya que la funcion no retorna nada
print(salida)
##########

def obtenerPromedio(diccionarioCalificaciones):
    promedio = sum(diccionarioCalificaciones.values()) / len(diccionarioCalificaciones)
    return promedio

diccionario = {"Cristian Pachon" : 3.0,"Alberto Alzate" : 4.0,"Anita Serpa" : 2.0,"Jessika Blandon" : 3.0}
salida = obtenerPromedio(diccionario)
print("promedio: ", salida)

##########
def productoDeNumeros(*numeros): # * Indica que se van a ingresar muchos parametros
    resultado = 1
    for numero in numeros:
        resultado = resultado * numero
    return resultado

salida1 =productoDeNumeros (3)
salida2 = productoDeNumeros(1,2,3,4)
salida3= productoDeNumeros(1,2,3,4,5,6)
print("productos", salida1, salida2, salida3)


