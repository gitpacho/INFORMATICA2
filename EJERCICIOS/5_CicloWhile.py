"""
Desarrolle un ciclo while infinito
"""
# condicion = True
# 
# while condicion:
#     print("ciclo ejecutado")

"""Cómo protegernos de un ciclo infinito"""

condicion = True
contador = 0
while condicion:
     print("ciclo ejecutado {}".format(contador))
     contador = contador + 1
     if contador == 100: 
        break

"""
Realice un ciclo while con un numero secreto. Cada vez que se ejecuta
un ciclo, el programa pide adivinar el numero, en caso de no ser acertado
se debe mostrar un mensaje diciendo: "Estás atrapado". Y en caso contrario
terminar el ciclo y avisar que el numero es correcto.
"""
#numero_secreto = 999
#numero_usuario = int(input("Ingrese el número secreto: "))
#condicion = (numero_secreto != numero_usuario)
#
#while condicion:
#    ...completar
#    print("No es el número correcto")
#    

"""
Realice un ciclo while que imprima los números del 10 al 100, separados por guion(-)
sin salto de linea
10 - 11 - 12 - 13 - ... 100
"""

print("\n\nEjercicios numeros del 1 al 100 ===> ")
#forma 1
contador = 10
lista = []
while (contador <= 100):
        lista.append(contador)
        contador = contador + 1
print(str(lista)[1:-1].replace(",", "-"))  

#forma 2
contador = 10
stringNumeros = ""
while (contador <= 100):
        stringNumeros = stringNumeros + str(contador) + "-"
        contador = contador + 1
print("\n", stringNumeros)


"""
Mostrar en pantalla los números del 200 al 100 utilizando ciclo while
"""

print("\n\nSecuencia 200 al 100 con salto de linea ======>")

contador = 200
while (contador>=100):
        print(contador, end="\n") #por defecto el end = "\n". Así que no es necesario escribirlo
        contador = contador - 1

"""
Mostrar en pantalla los números del 200 al 100 utilizando ciclo while
sin salto de linea
"""

print("\n\nSecuencia 200 al 100 sin salto de linea ======>")
contador = 200
while (contador>=100):
        print(contador, end=" ")
        contador = contador - 1


"""
Mostrar en pantalla los números del 200 al 100 utilizando ciclo while
ahora haga que el salto de linea se haga en cada 10 ciclos, así

200 199 198 197 196 195 194 193 192 191 
190 189 188 187 186 185 184 183 182 181 
180 179 178 177 176 175 174 173 172 171 
170 ...................................
.......................................
110 109 108 107 106 105 104 103 102 101
100
"""


print("\n\nSecuencia 200 al 100 con salto de linea cada 10 pasos  =====>")
#Forma 1
contador = 200
ciclo = 1
while (contador>=100):
        if ciclo < 10:
                ciclo = ciclo + 1
                print(contador, end=" ")
        elif ciclo == 10:
                ciclo = 1
                print(contador, end="\n")
        contador = contador - 1

#Forma 2
print("\n\n")
contador = 200
while (contador>=100):
        if (str(contador)[-1] in "098765432"):
                print(contador, end=" ")
        else:
                print(contador, end="\n")
        contador = contador - 1


"""
Pida a un usuario que ingrese numeros, en caso de que así lo desee.
De los numeros calcule cuál es el mayor de los ingresados.

Si el usuario no desea ingresar más números el ciclo debe terminar
"""

print("\n\n Ejercicio numero mayor ====>")
#Forma1 ========>
#respuesta = "si"
#mayor = -99999999
#while respuesta == "si":
#        respuesta = input("Desea ingresar un número: ")
#        if respuesta == "si":
#                numero = int(input("Ingrese el número: "))
#                if numero > mayor:
#                        mayor = numero
#        else:
#                respuesta = "no"
#print("El numero mayor es", mayor)

#Forma2 ========>
x="si"
lista = []
while x == "si":
        x = input("Desea ingresar un numero (si/no): ")
        if x == "si":
                n = int(input("Ingrese el número: "))
                lista.append(n)
        else:
                x = "no"

print(lista)
if len(lista)>0:
        print("MÁXIMO => ", max(lista))