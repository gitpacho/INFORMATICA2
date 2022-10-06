# 04-10-2022


#  Diccionarios y sus métodos

# Son elemetos compuestos por clave: valor

diccionario = {
                "Cristian Pachon": 3.0,
                "Daniel Quintero": 4.0,
                "Esteban Chavez": 5.0,
                "Margarita María": 3.0
              }

#Acceder a la calificacion de Cristian Pachon

print(diccionario["Cristian Pachon"])
print(diccionario["Margarita María"])
print(diccionario.get("Juan David Gonzalez", "no existe esta clave"))

try:
    print(diccionario["Juan David Gonzalez"])
except:
    print("Esto es un error, el programa continua")


# Extraer todas las claves del diccionario
print(diccionario.keys())

#Extraer todos los valores del diccionario
print(diccionario.values())


#Ejercicio: imprimir todas las claves de diccionario 
#           utilizando un ciclo for 
for key in diccionario.keys():
    print(key)

#Ejercicio: imprimir todos los valores del diccionario 
#           utilizando un ciclo for 
for value in diccionario.values():
    print(value)

#Ejercicio: imprimir todas las parejas clave-valor 
#           de diccionario utilizando un ciclo for 

for key in diccionario.keys():
    pareja = key + "-" + str(diccionario[key])
    print(pareja)    #Forma 1
    #print("{}-{}".format(key, diccionario[key])) #Forma2
    #print(key, "-", diccionario[key]) #con espacio #Forma3


# Imprimir las parejas utilizando el método items

for pareja in diccionario.items():
    print(pareja[0] + "-" + str(pareja[1]))

for key, value in diccionario.items(): #Desempaquetado
    print(key + "-" + str(value))


#Como cambiar los valores del diccionario
# Cambiar la calificacion de cristian a 5.0
diccionario["Cristian Pachon"] = 5.0
print(diccionario)

#Ejercicio: Cambiar todos los valores del diccionario
#           a 0.0

for key in diccionario.keys():
    diccionario[key] = 0.0

print(diccionario)

#Ejercicio Cambiar los valores del diccionario de la
#          siguiente manera:
#          * Si es hombre 0.0, si es mujer 5.0


for nombre in diccionario.keys():
    if nombre[-1] == "a":
        diccionario[nombre] = 5.0
    else:
        diccionario[nombre] = 0

print(diccionario)

# Haga una copia de diccionario y cambie las calificaciones
# a 5.0

diccionarioCopia = diccionario # Esto no es una copia real
diccionarioCopia = diccionario.copy() # Esto si es una copia real

for nombre in diccionarioCopia.keys():
    diccionarioCopia[nombre] = 5.0

print(diccionario, "no se ve afectado diccionario")
print(diccionarioCopia, "solo se ve afectado diccionarioCopia")


# Cómo eliminar un par clave:valor del diccionario ¿?
del diccionario["Cristian Pachon"]
print(diccionario)


#Ejercicio: Con lo visto anteriormente,
#           como cambiar la clave Margarita Maria
#           a Margarita Rosa

valor = diccionario["Margarita María"]
del diccionario["Margarita María"]
diccionario["Margarita Rosa"] = valor
print(diccionario)

#Almacene en un diccionario la siguiente base de datos
# de calificaciones
#Almacenelos de tal manera que sea posible acceder
# a la calificacion utilizando el nombre y la materia


""" 
                               Materias
    Nombre          Cuantica Etica Deportes Lenguas
Juan Gutierrez        2.0     5.0     1.3     3.2
Maria Snowden         3.1     4.9     2.2     1.1
Pedro Gonzalez        5.0     3.8     3.1     4.1
Angelica Lozano       2.1     2.7     4.1     3.2
Pablo Iglesias        3.2     1.6     5.0     1.2
Mariana Pajon         2.2     2.5     4.9     3.3
Esteban Loaiza        2.1     3.4     3.8     4.3
Daniela Pineda        5.0     4.3     2.7     1.2
Esteban Vazco         3.1     5.0     1.6     3.2
Enilse Lopez          5.0     2.2     2.5     5.0
Cristian Playonero    0.5     1.1     3.4     3.2
 """

#06-10-2022

#A pedal ===>  
calificaciones = {
    "Juan Gutierrez":     {"Cuantica" : 2.0,  "Etica": 5.0,  "Deportes": 1.3,  "Lenguas": 3.2},
    "Maria Snowden":      {"Cuantica" : 3.1,  "Etica": 4.9,  "Deportes": 2.2,  "Lenguas": 1.1},
    "Pedro Gonzalez":     {"Cuantica" : 5.0,  "Etica": 3.8,  "Deportes": 3.1,  "Lenguas": 4.1},
    "Angelica Lozano":    {"Cuantica" : 2.1,  "Etica": 2.7,  "Deportes": 4.1,  "Lenguas": 3.2},
    "Pablo Iglesias":     {"Cuantica" : 3.2,  "Etica": 1.6,  "Deportes": 5.0,  "Lenguas": 1.2},
    "Mariana Pajon":      {"Cuantica" : 2.2,  "Etica": 2.5,  "Deportes": 4.9,  "Lenguas": 3.3},
    "Esteban Loaiza":     {"Cuantica" : 2.1,  "Etica": 3.4,  "Deportes": 3.8,  "Lenguas": 4.3},
    "Daniela Pineda":     {"Cuantica" : 5.0,  "Etica": 4.3,  "Deportes": 2.7,  "Lenguas": 1.2},
    "Esteban Vazco":      {"Cuantica" : 3.1,  "Etica": 5.0,  "Deportes": 1.6,  "Lenguas": 3.2},
    "Enilse Lopez":       {"Cuantica" : 5.0,  "Etica": 2.2,  "Deportes": 2.5,  "Lenguas": 5.0},
    "Cristian Playonero": {"Cuantica" : 0.5,  "Etica": 1.1,  "Deportes": 3.4,  "Lenguas": 3.2},
}

#Automaticamente =>
data = [["Juan Gutierrez",        2.0,     5.0,     1.3,     3.2],
        ["Maria Snowden",         3.1,     4.9,     2.2,     1.1],
        ["Pedro Gonzalez",        5.0,     3.8,     3.1,     4.1],
        ["Angelica Lozano",       2.1,     2.7,     4.1,     3.2],
        ["Pablo Iglesias",        3.2,     1.6,     5.0,     1.2],
        ["Mariana Pajon",         2.2,     2.5,     4.9,     3.3],
        ["Esteban Loaiza",        2.1,     3.4,     3.8,     4.3],
        ["Daniela Pineda",        5.0,     4.3,     2.7,     1.2],
        ["Esteban Vazco",         3.1,     5.0,     1.6,     3.2],
        ["Enilse Lopez",          5.0,     2.2,     2.5,     5.0],
        ["Cristian Playonero",    0.5,     1.1,     3.4,     3.2]]

diccionarioCalificaciones = {}
for estudiante in data:
  diccionarioCalificaciones[estudiante[0]] = {"Cuantica": estudiante[1], "Etica":estudiante[2] ,
                                              "Deportes":estudiante[3], "Lenguas":estudiante[4]}
print(diccionarioCalificaciones)

"""
Calcular el promedio de calificaciones de cada estudiante usando diccionarioCalificaciones
Determinar los 3 estudiantes con mejor y peor promedio
Calcular el promedio de las 4 materias
"""









