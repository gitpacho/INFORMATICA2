class Estudiante:
    def __init__(self, nombre, edad, codigo, notas):
        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.notas = notas

    def calcularPromedio(self):
        promedio = sum(self.notas)/len(self.notas)
        return promedio

    def determinarMejorNota(self):
        mejorNota = max(self.notas)
        return mejorNota

    def determinarPeorNota(self):
        peorNota = min(self.notas)
        return peorNota


class Curso:
    def __init__(self, nombreCurso, nombreProfesor, estudiantes):
        self.nombreCurso = nombreCurso
        self.nombreProfesor = nombreProfesor
        self.estudiantes = estudiantes #lista de estudiantes, diccionario ....

    def calcularMediaDelCurso(self):
        media = sum(self.estudiantes.values())/len(self.estudiantes)
        return media

    def determinarEstudiantesAprobados(self):
        Aprobados= []
        for nombre in self.estudiantes:
            if self.estudiantes[nombre] >= 3.0:
                Aprobados.append(nombre)
        return Aprobados

    def determinarEstudiantesReprobados(self):
        pass



if __name__ == "__main__":
    estudiante1 = Estudiante("Cristian Pachon", 20, "019", [5.0, 1.0, 3.0])
    data = {
    "Cristian P": 1.5,
    "Maria Jimenes": 4,
    "Oscar Agudelo":3.5}

    print(estudiante1.calcularPromedio())

    curso1 = Curso("Matematicas", "Cristian Pachon", data)
    print("media del curso=>", curso1.calcularMediaDelCurso())

    
