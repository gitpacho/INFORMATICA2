#10-11-2022

"""
Ejercicio:
    1)  Crear una clase llamada Profesores
        con los atributos: nombre, edad, salario
        con los metodos: enseñar, calificar
"""


class Profesores:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def enseñar(self, calidad):
        return "estoy enseñando al {} %".format(calidad)
    
    def calificar(self, estadoAnimo):
        if estadoAnimo == "feliz":
            return "su no ta es 5.0"
        elif estadoAnimo == "triste":
            return "su nota es 0.0"

if __name__ == "__main__":
    profesor1 = Profesores("Elisabeth Restrepo", 20, 15000000)
    profesor2 = Profesores("Luis Mulcue", 50, 5000000)

    print(profesor1.nombre)
    print(profesor2.salario)
    print(profesor1.enseñar(20))
    print(profesor2.calificar("triste"))