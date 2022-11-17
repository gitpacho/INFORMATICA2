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
        self.estudiantes = estudiantes #lista con objetos de la clase Estudiantes

    def calcularMediaDelCurso(self):
        suma = 0
        numero_estudiantes = len(self.estudiantes)
        for estudiante in self.estudiantes:
            suma = suma + estudiante.calcularPromedio()
        promedio_Curso = suma/numero_estudiantes
        return promedio_Curso


        
        


    def determinarEstudiantesAprobados(self):
        pass

    def determinarEstudiantesReprobados(self):
        pass
        
        
        
        



if __name__ == "__main__":
    estudiante1 = Estudiante("Cristian Pachon", 20, "019", [0.0, 0.0, 1.5])
    estudiante2 = Estudiante("Maria Jimenez", 15, "020", [5.0, 2.0, 5.0])
    estudiante3 = Estudiante("Lesly Cañas", 19, "021", [5.0, 5.0, 5.0])
    listaEstudiantes = [estudiante1, estudiante2, estudiante3]

    curso1 = Curso("Matematicas", "Cristian Pachon", listaEstudiantes)

    print("media del curso=>", curso1.calcularMediaDelCurso())
    print("aprobados", curso1.determinarEstudiantesAprobados())
    print("reprobados", curso1.determinarEstudiantesReprobados())


    print(listaEstudiantes)

    
