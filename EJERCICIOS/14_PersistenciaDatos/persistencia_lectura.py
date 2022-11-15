#15-11-2022

#---------- Lectura de archivos json


"""Leer el archivo DATA.json
y luego calcular la media de los valores
"""

import json
archivo = "DATA.json"
ruta = "EJERCICIOS/14_PersistenciaDatos/" + archivo
opcion = "r" #lectura

with open(ruta, opcion) as file:
    data = json.load(file)

print("media=>", sum(data)/len(data))


"""
Leer el archivo estudiantes.json y luego calcular el promedio
de cada uno de los estudiantes
"""

archivo = "estudiantes.json"
ruta = "EJERCICIOS/14_PersistenciaDatos/" + archivo
opcion = "r"

with open(ruta, opcion) as file:
    data = json.load(file)

for nombre in data.keys():
    print(nombre, " => ", sum(data[nombre])/3)









