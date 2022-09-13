
#  13-09-2022
#  Ejercicios métodos de strings

cadena = "MundoCruel"

"""
Buscar métodos que hagan lo siguiente:
    * Retornar caracteres en mayusculas
    * Retornar caracteres en minusculas
    * Retornar el numero de veces que se repite un caracter
    * Retornar si la cadena es alfabetica
    * Retornar si la cadena es alfanumerica
    * Retornar si la cadena contiene numeros
    * Reemplazar una letra o palabra por otra 
"""

cadena.upper()     #===> Retorna una nueva cadena en mayuscula
cadena.lower()     #===> Retorna una nueva cadena en minuscula
cadena.count("M")  #===> Retorna un entero, como conteo del numero de veces que se repite un string
cadena.isalpha()   #===> Retorna un booleano, como respuesta a la pregunta: ¿Es alfabético?
cadena.isalnum()   #===> Retorna un booleano, como respuesta a la pregunta: ¿Es alfanumérico?
cadena.isnumeric() #===> Retorna un booleano, como respuesta a la pregunta: ¿Es numérico?
cadena.replace("Cruel", "Feliz")  #===> Retorna una nueva cadena, con algún elemento reemplazado

# Las cadenas son inmutables, ningún método la puede alterar
# por mucho se puede generar otra cadena, pero no se afecta a la original


#----------------------------------------------------------------------------

#====== Indexación y slicing

# Indexado: operación para extraer caracteres ubicados en un indice. Ejemplo: cadena[indice]
# Slicing es la operación para extraer rebanadas de una cadena. Ejemplo: cadena[inicio:fin:salto]


cadena = "Mundo UnalA"

#cadena de 2 en 2
cadena[0:len(cadena):2]

#cadena al revés
cadena[-1::-1]

#elementos ubicados en las posicions 3,5 y 7
cadena[2:8:2]

#elementos hasta la mitad de la cadena
cadena[0:5]

#elementos de la mitad en adelante de la cadena
print(cadena[6:11])

#elementos desde la mitad de la cadena hasta el primer elemento
cadena[4::-1]



#---------------------Ejercicios de practica -----------------

cadena = "Anita no lava la tina de lunes a viernes"
# Extraer el primer elemento
# Extraer el ultimo elemento
# extrar los dos elementos de la mitad
# Extraer la cadena al revés
# Extraer del 10mo al 15avo elementos al revés
# Extraer cada 10mo elemento


"""
Buscar y utilizar métodos para hacer lo siguiente:
    * pasar la cadena a mayusculas
    * pasar la cadena a minusculas
    * reemplazar la palabra Anita y colocar su nombre
    * pasar la cadena a formato de titulo
    * contar el numero de veces que aparecen las vocales
"""