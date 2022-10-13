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
interfaz.separador("--")
logica.sumar3Numeros(1,2,3)
logica.sumarNumeros(1,2,3,4,5,6,7,8,9)
logica.sumarListas([1,2,3], [3,2,1])





