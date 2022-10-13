import interfaz


print(dir(interfaz))
print(interfaz.__doc__)
print(interfaz.__file__)

interfaz.separador("@")
interfaz.separador("-")
interfaz.imprimirNombre("Cristian")
respuesta = [1,2,3]
interfaz.imprimirVariable("Respuesta", respuesta)


import logica
resultado1 = logica.sumar3Numeros(1,2,3)
resultado2 = logica.sumarNumeros(1,2,3,4,5,6,7,8,9)
resultado3 = logica.sumarListas([1,2,3], [3,2,1])

interfaz.separador("-")
interfaz.imprimirVariable("sumar 3 numeros", resultado1)
interfaz.imprimirVariable("sumar N numeros", resultado2)
interfaz.imprimirVariable("sumar 2 listas", resultado3)
interfaz.separador("-")