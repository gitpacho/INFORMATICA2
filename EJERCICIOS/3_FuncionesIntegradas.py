
# 01-09-2022
#Utilizaremos las funciones integradas más comunmente usadas

########## Funciones entrada/salida ############

# ---------------------- Funcion input y print -----------------------
#nombre = input("Ingrese su nombre: ") # Interrumpir la ejecucion del codigo, hasta que se almacene un valor                                      
#print("Su nombre es ", nombre)

#Solicite una edad y muestre por pantalla "si es mayor de edad" o "no es mayor de edad"
#edad = input("Ingrese su edad :")
#edad = int(edad)
#print((edad >= 18 and "es mayor de edad") or "no es mayor de edad")

#Solicite una clave y muestre por pantalla si es correcta o incorrecta. Clave ==> 9876
#clave_original = 9876
#clave_entrada = int(input("Ingrese la clave: "))
#print((clave_original == clave_entrada and "correcto") or "incorrecto")


# ---------------------- funcion format ---------------------------
numero = 192.5678
formato_cientifico = format(numero, "e")
print("formato_cientifico ===> ", formato_cientifico)
formato_cientifico = format(numero, ".2e")
print("formato_cientifico (con 2 decimales) ===> ", formato_cientifico)
formato_cientifico = format(numero, ".0e")
print("formato_cientifico (con 0 decimales) ===> ", formato_cientifico)

numero = 12.90939001                           # Aproxima de manera correcta
formato_flotante = format(numero, ".2f")
print("formato flotante (2 decimales) ===>", formato_flotante)
formato_flotante = format(numero, ".0f")
print("formato flotante (0 decimales) ===>", formato_flotante) 


"""
      a) 0.52941, 2.389,  ==>   entero
                                flotante 2 decimales, 
                                flotante 5 decimales,
                                notación científica 1 decimal,
                                notación científica 2 decimales,
"""

cadena = "hola mundo"
formato_centrado =  format(cadena, "^50")
formato_derecha =  format(cadena,  ">50")
formato_izquierda = format(cadena, "<50") 

print("formato cen ==> \n",  formato_centrado)
print("formato der ==> \n",  formato_derecha)
print("formato izq ==> \n ", formato_izquierda)



#------------------ Funciones de conversión ----------
# convertir a binario, octal y hexadecimal

decimal = 102
conversion_binario = bin(decimal) 
conversion_octal   = oct(decimal)
conversion_hex     = hex(decimal)

print("====   Decimal   ===> ", decimal)
print("bin, oct, hex ===>", conversion_binario, conversion_octal, conversion_hex)


"""
¿Cómo hacer lo contrario?
bin==> decimal
oct ==> decimal
hex ==> decimal
"""

bin, oct, hex = "1100110", "146", "66"

print("bin a decimal ==> ", int(bin, 2))
print("oct a decimal ==> ", int(oct, 8))
print("hex a decimal ==> ", int(hex, 16))



#-------------------- funciones de ayuda (dir)----------

cadena = "holamundo"
lista = [1,2,3]
entero = 10

print("\n funcionalidades para cadena ==> \n\n" , dir(cadena))
print("\n funcionalidades para lista ==>  \n\n" , dir(lista))
print("\n funcionalidades para entero ==> \n\n" , dir(entero))


# ------------------ funciones para secuencias -----------


print("\n\n Funciones para secuencias ====> ")


#numeros del 1 al 10
secuencia = range(1, 11)  #El inicio se toma, pero el final no se toma, cuando el salto es 1, no es necesario el tercer parámetro
print(list(secuencia))

#numeros del 20 al 29
secuencia = range(20, 30)   #
print(list(secuencia))

#numeros del -10 al 10 con salto 2
print(list(range(-10, 11, 2)))
#numeros multiplos de 3 desde el -10 hasta el 5
print(list(range(-9,6,3)))
#numeros del 10 al 0
print(list(range(10, -1, -1)))
#numeros multiplos de 3 y 5 del 1 al 1000. Al revés
print(list(range(990, 0, -15)))

#------------------------------
#Tamaño: len()
#Suma: sum()
#Min: min()
#Max: max()
#reversa: reversed()

secuencia = range(1, 10000, 3)
lista = [1, 2, 3, 5, 8, 8, 9, 1]

print("tamaño secuencia ==>", len(secuencia))
print("tamaño lista     ==>", len(lista))

print("minimo de secuencia ==>", min(secuencia))
print("maximo de lista     ==>", max(lista))

print("revertir secuencia ==>", list(reversed(secuencia)))
print("revertir lista     ==>", list(reversed(lista)))

#Repetir el ejercicio anterior usando reversed







