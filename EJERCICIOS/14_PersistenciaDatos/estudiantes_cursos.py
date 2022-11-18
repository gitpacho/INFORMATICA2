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
    def __init__(self, nombreCurso, nombreProfesor):
        self.nombreCurso = nombreCurso
        self.nombreProfesor = nombreProfesor
        
        import json
        ruta = "EJERCICIOS/14_PersistenciaDatos/dataEstudiantes.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        print("lectura de datos=>", data)

        listaEstudiantes = []
        for diccionarioEstudiante in data:
            nombre = diccionarioEstudiante["nombre"]
            edad = diccionarioEstudiante["edad"]
            codigo = diccionarioEstudiante["codigo"]
            notas = diccionarioEstudiante["notas"]
            objetoEstudiante = Estudiante(nombre,edad,codigo,notas)
            listaEstudiantes.append(objetoEstudiante)

        self.estudiantes = listaEstudiantes

    def calcularMediaDelCurso(self):
        suma = 0
        numero_estudiantes = len(self.estudiantes)
        for estudiante in self.estudiantes:  #Recorro lista estudiantes
            suma = suma + estudiante.calcularPromedio()
        promedio_Curso = suma/numero_estudiantes
        return promedio_Curso

    def determinarEstudiantesAprobados(self):
        aprobados = []
        for estudiante in self.estudiantes:
            promedio_estudiante = estudiante.calcularPromedio()
            if promedio_estudiante >= 3.0:
                aprobados.append(estudiante.nombre)
        return aprobados

    def determinarEstudiantesReprobados(self):
        reprobados = []
        for estudiante in self.estudiantes:
            promedio_estudiante = estudiante.calcularPromedio()
            if promedio_estudiante < 3.0:
                reprobados.append(estudiante.nombre)
        return reprobados


if __name__ == "__main__":
    curso1 = Curso("Matematicas", "Elisabeth Restrepo")

    print("media del curso=>", curso1.calcularMediaDelCurso())
    print("aprobados", curso1.determinarEstudiantesAprobados())
    print("reprobados", curso1.determinarEstudiantesReprobados())