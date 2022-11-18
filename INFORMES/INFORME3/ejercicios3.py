nombre_completo = ""   #Por favor ingrese su nombre COMPLETO en la cadena

# ----------------------------Ejercicios INFORME 3--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - No hay necesidad de escribir las preguntas en su archivo ejercicios3.py
"""


# ------------------------ EJERCICIO 1 --------------------------------
"""
    Cree los modulos: logicaTriqui, interfazTriqui, controlTriqui (en la carpeta INFORME3) para jugar triqui
    Utilice los codigos vistos en clase para basarse. Debe hacer que el jugador 2 sea automatico.
"""

# ------------------------ EJERCICIO 2 --------------------------------
"""
    Cree los modulos: decimal, binario, octal, hexadecimal, control (en la carpeta INFORME3)
    El modulo decimal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)

    El modulo binario debe tener las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (cadena_decimal)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal)

    El modulo Octal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_octal), retorna string (cadena_binario)
            convertirADecimal     => recibe string (cadena_octal), retorna string (cadena_decimal)
            convertirAHexadecimal => recibe string (cadena_octal), retorna string (cadena_hexadecimal)

    El modulo Hexadecimal debe tener las siguientes funciones:
            convertirABinario => recibe string (cadena_hexadecimal), retorna string (cadena_binario)
            convertirADecimal => recibe string (cadena_hexadecimal), retorna string (cadena_decimal)
            convertirAOctal   => recibe string (cadena_hexadecimal), retorna string (cadena_Octal)

    El modulo control queda a su disposicion:
            Servirá para mostrar las opciones de conversion
            y realizar el control del programa (realice las sentencias que considere necesarias)
            
"""

# ------------------------ EJERCICIO 3 --------------------------------
"""
La siguiente tabla muestra el diseño en programación orientada a objetos de diferentes tipos de autos.
----------------------------------------------------------------------------
CLASE     =>   Automoviles
OBJETOS   =>   FERRARI_458          |   MCLAREN_720S          |  AUTOLEGAL
ATRIBUTOS =>   "rojo"(color)        |   "negro" (color)       |  "blanco" (color)
               2 (personasSentadas) |   4 (personasSentadas)  |  20 (personasSentadas)
               "Deportivo" (uso)    |   "Deportivo" (uso)     |  "Publico" (uso)
MÉTODOS   =>   acelerar, frenar     |   acelerar, frenar      |  acelerar, frenar
----------------------------------------------------------------------------

 Debe crear la clase Automoviles
    Atributos => color (str)
                 personasSentadas (int)
                 uso (str)
    Metodos => acelerar, frenar
               El metodo acelerar debe recibir la aceleración (a) y tiempo (t) empleado por el vehículo. Debe retornar la velocidad alcanzada (v = a * t)
               El metodo frenar debe recibir la velocidad (v) y desaceleracion (a) empleada por el vehículo. Debe retornar el tiempo de detención (t = -v/a)

 Luego debe crear los objetos: FERRARI_458, MCLAREN_720S, AUTOLEGAL 

    Este ejercicio se evaluará revisando cada objeto => FERRARI_458, MCLAREN_720S, AUTOLEGAL
    se verifica que los atributos sean los correctos y los metodos funcionen adecuadamente
"""


# ------------------------ EJERCICIO 4 --------------------------------
"""
Revise el archivo empleados.json para realizar este ejercicio:

Cree la clase Empresa con los siguientes atributos y metodos:
    atributos =>  nombre (str)
                  ciudad (str)
                  empleados (lista vacia [])
    metodos =>  cargarEmpleados(rutaArchivo)                                       # Debe cargar los empleados.json en el atributo empleados
                leerEmpleados()                                                    # Debe retornar una lista con el nombre de todos los empleados
                agregarNuevoEmpleado(nombre, codigo, edad, cargo, añosExperiencia) # Debe almacenar un nuevo empleado en empleados.json
                eliminarEmpleado(codigo)                                           # Debe eliminar el diccionario cuyo codigo corresponda en empleados.json

Luego, cree un objeto empresa1 cuyo nombre es "software Colombia" y ciudad "manizales" de la siguiente manera:
    empresa1 = Empresa("software Colombia", "manizales")

Ejecute los metodos:
    empresa1.cargarEmpleados("INFORME3/empleados.json")
    empresa1.agregarNuevoEmpleado("Juan Posada", "100", 30, "Jefe", 1)
    empresa1.eliminarEmpleado("001")
    empresa1.eliminarEmpleado("002")
    empresa1.eliminarEmpleado("003")
    empresa1.cargarEmpleados("INFORME3/empleados.json")
    
Finalmente muestre sus resultados en una lista llamada listaEmpleados =>
listaEmpleados = empresa1.leerEmpleados()
"""


#---------------Ejercicio opcional ---------------------

"""
cree los modulos: logicaSudoku, interfazSudoku, controlSudoku para jugar un sudoku 4*4
utilice las variables y sentencias que crea conveniente
"""