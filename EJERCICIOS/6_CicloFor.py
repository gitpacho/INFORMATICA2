#08-09-2022

"""Recorrer los siguientes iterables"""
cadena = "HolaMundoCruel"
lista = [1,2, 30, 100, 50, -20]
tupla = (1,2,3,1,2,3,1,2,3)
resultados = [1,-1,1,-1,1,-1]
rango = range(1,100)

print("Recorrido de cadena  ==> ")
for caracter in cadena:
    print(caracter, end="--")

print("\n\nRecorrido de lista ==> ")
for i in lista:
    print(i, end= "--")

print("\n\nRecorrido de tupla ==> ")
for numero in tupla:
    print(numero, end= "--")

print("\n\nRecorrido de resultados  ==> ")
for resultado in resultados:
    print(resultado, end= "  ")

print("\n\nRecorrido de rango  ==>")
for i in rango:
    print(i, end="--")

"""
Recorrer los números  del 1 al 10 utilizando diferentes iterables (por lo menos 4)
sin necesidad de definirlos en una variable
"""

#forma 1
print("\n\nForma 1 =>")
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end= "  ")

#forma 2
print("\nForma 2 =>")
for i in range(1,11):
    print(i, end= "  ")

#forma 3
print("\nForma 3 =>")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i, end= "  ")
    
#forma 4
print("\nForma 4 =>")
for i in "12345678910":
    print(i, end = "  ")

"""
 Imprimir los numeros pares del 0 al 20
"""
print("\n\n Numeros pares")
for i in range(0, 21, 2):
    print(i, end=" ")


"""
Imprimir los números multiplos de 4 desde el 5 hasta 30
"""

print("\n\n Opción 1 numeros multiplos de 4")
for i in range (8,29,4):
    print (i, end="   ")

print("\n\n Opción 2 numeros multiplos de 4")
for m in range(5,31):
    if m%4 == 0:
        print(m)