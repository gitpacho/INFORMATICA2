#06-09-2022

"""
Pida a un usuario su nombre y su edad. Determine si es mayor de edad,
y muestre un mensaje en pantalla diciendo:
<NOMBRE>, usted es mayor/menor de edad
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese la edad: "))

if 18<=edad<=150:
    print("{}, usted es mayor de edad".format(nombre))
elif 0<edad<18:
    print("{} usted es menor de edad".format(nombre))

"""
Realice un programa que calcule 
el mayor de tres números
"""
a = 3
b = 5
c = 5
if a>=b and a>=c:
   print("{} es el numero mayor".format(a))
elif b>=a and b>=c:
    print("{} es el numero mayor".format(b))
elif c>=a and c>=b:
    print("{} es el numero mayor".format(c))

"""
*salario base = 1 000 000 
Realice un programa que
calcule el salario de un vendedor
de seguros,teniendo en cuenta 
las siguientes condiciones =>

=> ventas => entre [5, 20] seguros => 
              aumento del 20% sobre la base
=> ventas => entre [21, 50] seguros => 
              aumento del 30% sobre la base
=> ventas =>  entre [51, infinito] seguros => 
              aumento del 35% sobre la base

"""

salario_base = 1_000_000
ventas = int(input("Numero de ventas: "))
salario_total = 0
condicion1 = (5 <= ventas <= 20)
condicion2 = (21 <= ventas <= 50)
condicion3 = (ventas >= 51)

if condicion1:
    salario_total = salario_base + 0.2 * salario_base 
elif condicion2:
    salario_total = salario_base + 0.3 * salario_base 
elif condicion3:
    salario_total = salario_base + 0.35 * salario_base 
print("El salario total es {}".format(salario_total))


"""
Una contraseña de un programa, debe incluir:

* Contenga mayusculas
* Contenga minusculas
* Contenga números
* Caracteres especiales
* Por lo menos 8 caracteres en total

Determine si al ingresar una contraseña, esta cumple con todas las 
anteriores condiciones. """

#contraseña = "jsfdlkLJKJ5678/&%$"
#validez = False
#
#condicion1 = <Contenga mayusculas>
#condicion2 = <Contenga minusculas>
#condicion3 = <Contenga números>
#condicion4 = <Caracteres especiales>
#condicion5 = <Por lo menos 8 caracteres en total>
#
#if (condicion1 and condicion2 and condicion3 and condicion4 and condicion5):
#    validez = True
#else:
#    validez = False
#
#print("Es valida o no")




















