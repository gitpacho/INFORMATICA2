# ----------------------------Ejercicios INFORME 1--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de re-escribir las preguntas en su archivo
 - Muestre sus procedimientos de manera clara
""" 

#------------------------ EJERCICIO 1 --------------------------------
"""
Cree los siguientes rangos (tipo range()): 
   rango1 => 334, 331, 328, 325, ... 4, 1
   rango2 => 1, 3, 5, 7, 9, 11, ... 999, 1001
   rango3 => -50, -55, -60, -65, -70, ... -195, -200

Después de obtener los rangos, almacenelos de la siguiente manera:
listaDeRangos = [rango1, rango2, rango3]
"""

#------------------------ EJERCICIO 2 --------------------------------
""" 
    Seis diferentes autos realizan una carrera. 
    Cada uno de ellos empieza su recorrido en intervalos de 2 segundos

El primero de ellos inicia su recorrido y acelera a razón constante de 1.5m/s²
El segundo inicia su recorrido 2 segundos después a razón de 2 m/s². 
El tercero inicia su recorrido 4 segundos después a razón de 3 m/s². 
El cuarto inicia su recorrido 6 segundos después a razón de 3.5 m/s². 
El quinto inicia su recorrido 8 segundos después a razón de 4 m/s². 
El sexto inicia su recorrido 10 segundos después a razón de 4.5 m/s².

¿qué auto realiza el primer rebase sobre otro auto?

Almacene su respuesta en un string llamado primerRebase. Ejemplo: 
primerRebase = "Auto6-Auto3"  (auto que rebasa - auto rebasado)

"""

#------------------------ EJERCICIO 3 --------------------------------
"""Los estudiantes del curso de matematicas obtuvieron las siguientes 
calificaciones definitivas (cada una de las notas equivale al 25%):

         Examen1  Examen2  Examen3  Examen4
Camila    1.0      2.3       5.0      5.0
Maria     5.0      3.5       2.5      3.2
José      2.2      4.0       3.2      4.1
Daniela   5.0      0.5       1.0      0.2
Esteban   4.0      5.0       0.0      0.0

El director del grupo preparará una salida académica, en caso de 
que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia. (se aprueba en 3.0)
   * Por lo menos dos examenes del grupo, deben tener un promedio mayor a 3.0
   * Todos los que perdieron la materia deben tenerla por encima de 2.0

¿habrá salida académica?
Almacene la respuesta en una variable denominada => salidaAcademica, cuyo valor sea un booleano
si salen => True, si no salen => False
"""

#------------------------ EJERCICIO 4 --------------------------------

""" El salario mensual de un empleado se calcula solo teniendo en cuenta el numero de seguros vendidos,
    (el precio de cada seguro es de $120000)

    Para los primeros 20 seguros vendidos, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.

   El salario de 4 empleados es el siguiente:

    Empleado   Empleado1   Empleado2    Empleado3   Empleado4
    Salario   $ 7860000    $ 5520000   $ 3720000    $ 2280000

   Determine el numero de seguros vendidos por cada empleado.
   Almacene su respuesta en una lista llamada cantidadSegurosVendidos como muestra el ejemplo:
   cantidadSegurosVendidos = [10, 50, 80, 32]
"""

#------------------------ EJERCICIO 5 --------------------------------

""" La calificación de una materia se encuentra en el intervalo [0.0 ,5.0] 
y se calcula tomando 4 notas, con porcentajes de 15%, 25%, 20% y 40%.
Si los estudiantes tienen las primeras 3 calificaciones definidas.
Calcule la nota4 necesaria  para aprobar la materia. (se aprueba en 3.0)

   Nombre          Nota1   Nota2  Nota3  Nota4  
Maria Gonzalez       3.1    3.1    1.2      ?
Camilo Suarez        3.2    4.0    1.1      ?
Esteban Rodriguez    3.2    4.1    2.2      ?
Mariana Rosero       5.0    5.0    5.0      ?
Jose Nuñez           5.0    4.0    2.5      ?
Esteban Quesada      3.4    4.0    2.6      ?
Mauricio Velazquez   5.0    4.2    2.1      ?
Julia Quintero       2.0    2.2    2.1      ?
Mauricio Lizcano     3.7    4.1    4.7      ?
Miguel Pineda        1.0    1.1    3.3      ?
Angie Gomez          4.1    4.7    4.4      ?
Angelica Lozano      3.1    1.0    2.6      ?
Camilo Restrepo      5.0    5.0    1.0      ?

Almacene los resultados en un diccionario llamado notasNecesarias,
cuya clave sea el nombre completo del alumno (string) y el valor
sea la nota necesaria del respectivo alumno (flotante con 2 decimales)

Ejemplo:  notasNecesarias = {"Maria Gonzalez": 3.87, "Mauricio Velazquez": 2.31, ...}
"""