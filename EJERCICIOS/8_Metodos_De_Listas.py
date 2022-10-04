#29-09-2022

# Métodos de las listas

lista = [1, "a", 2, 3, "b"]
print(lista.append("1000"))
print(lista.append(10))
print(lista)
print(lista.pop(1))
print(lista.pop(4))
print(lista)


## --------------EJERCICIOS CLASE-------------
''' Sumar los elementos que se pueden sumar algebraicamente '''


lista2 = [1, 2, 'Cristian', 3, 'b', 'Pachon', 10]
print("---- sumar elementos algebraicos ---")
#----forma1
lista2.pop(5)
lista2.pop(4)  
lista2.pop(2)
print(sum(lista2))

#---forma2
 #lista2.pop(2)
 #lista2.pop(3)
 #lista2.pop(3)
 #print(sum(lista2))

#----forma3
#for indice in [2,3,3]:
#  lista2.pop(i)
 #print(sum(lista2))

"""2) Sumar los elementos que se pueden sumar algebraicamente sin afectar lista3 """
print("-------Sumar sin afectar la lista original-----")

lista3 = [1, 2, 100, 3, 'b', 'Pachon', 10, "holamundo", 5]
lista3Copia = lista3.copy()
lista3Copia.pop(4)
lista3Copia.pop(4)
lista3Copia.pop(5)
print("lista original sin afectar => ", lista3)
print("lista3 copia afectada => ", lista3Copia)
print("suma resultante =>", sum(lista3Copia))

"""3) Organice los elementos de la lista3Copia con el metodo sort. ¿Es inplace? """

print("-------Organizar lista 3 (copia)-----")
lista3Copia.sort()  #Por defecto ordena de forma ascendente
print(lista3Copia)




"""Metodos Indexado y Slicing"""
print("----Ejercicios indexado y slicing----------")
listaNueva = [1, 2, 3, 4, 5, "hola", "cruel", "mundo", 100]

#Indexado
#Extraer el primer elemento de 2 maneras
print(listaNueva[0], listaNueva[-9])
#Extraer el ultimo elemento de dos maneras
print(listaNueva[8], listaNueva[-1])
#Extraer el elemento de la mitad de dos maneras
print(listaNueva[4] + [listaNueva[-5]])



#Slicing
#Extraer cada elemento de dos en dos => 1, 3, 5, "Cruel", 100
print(listaNueva[0:9:2], listaNueva[0:9:2])
#Extraer hasta la mitad de la cadena => 1,2,3,4,5
print(listaNueva[0:5:1], listaNueva[0:5:], listaNueva[0:5])
#Extraer desde la mitad de la lista en adelante => 5, "hola", "cruel", "mundo", 100
print(listaNueva[4:9:1], listaNueva[4:9], listaNueva[4::])
#Extraer los elementos que son strings => "hola", "cruel", "mundo"
print(listaNueva[5:8])
#Extraer los elementos que son enteros => 1, 2, 3, 4, 5, 100
print(listaNueva[0:5] + [listaNueva[-1]])

