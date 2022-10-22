
nombre_completo = ""   #Por favor ingrese su nombre COMPLETO en la cadena


# ----------------------------Ejercicios INFORME 2--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de escribir las preguntas en su archivo 
 - Muestre sus procedimientos de manera clara
""" 


#------------------------ EJERCICIO 1 --------------------------------
""" El rendimiento deportivo de un grupo de atletas es el siguiente ("A" es alto, "B" aceptable  y "C"  insuficiente.):

Cod. Deportista (str) =>   001   002   003   004   005   006   007   008   009    010   011   012    013    014    015    016    017   018  019  020  021  022   023   024   025  026  027   028   029   030   031   032   033    034    035   036    037   038   039   040 041   042   043   044   045  046   047   048   049   050   051  052    053    054   055   056   057   058   059  060  061   062   063   064   065   066  067   068   069   070   071   072   073    074   075   076    077   078   079   080   081   082   083   084   085  086   087   088   089   090   091  092    093    094   095    096   097  098  099  100
rendimiento     (str) =>   A     B     C     B     B     B     C     B     A      C     B     A      C      B      B      B      B     A    B    A    A    C     B     B     B    B    C     B     B     C     B     A     C      B      A     C      B     B     B     C   B     C     B     A     C     B    A     C     B     B     B    B      A      B     A     A     C     B     B    B    B     C     B     B     C     B    A     C     B     A     C     B     B      B     C     A      B     C     B     B     A     B     C     B     B    B     B     B     A     B     B    A      C      B     B      B     B    A    B    B  
edad            (int) =>   42    60    18    20    35    25    60    30    19     42    21    17     39     30     28     34     27    23   12   20   23   20    25    40    31   32   45    26    17    15    19    30    35     22     12    20     15    40    40    14  32    62    18    22    35    26   62    32    19    32    21   17     39     32    28    33    27    23    12   22   23    22    26    32    31    32   36    26    17    16    19    32    36     22    12    22     16    32    32    13    42    60    18   20    35    25    60    30    19    42    21   17     39     30    28    34     27   23   12   20

Cree 3 diccionarios cuyos nombres son ==> rendimientoAlto, rendimientoAceptable, rendimientoInsuficiente
Luego almacene los deportistas en su respectivo diccionario, utilizando como clave el codigo del deportista y como valor su edad.

¡OJO! => Almacene la respuesta de la siguiente manera:
deportistas = [rendimientoAlto, rendimientoAceptable, rendimientoInsuficiente]
"""

#------------------------ EJERCICIO 2 --------------------------------
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,con la siguiente información

     |                    Informacion
Cod  |  Nombre               Cargo          Salario   
---- |  ------------------------------------------------
001  |  Cristian Pachon     Ingeniero       3200000
002  |  Daniela Pineda      Programador     4300000
003  |  Esteban Murcia      Programador     4600000
004  |  Jose Guzman         Ingeniero       3900000
005  |  Camilo Rodriguez    Ensamblador     1200000
006  |  Mariana Londoño     Ensamblador     1100000
007  |  Estefania Muños     Ensamblador     1700000
008  |  Cristian Rodriguez  Ingeniero       3100000
009  |  Natalia Alzate      Ensamblador     2200000
010  |  Juan Sanabria       Diseñador       5100000
011  |  Juanita Calderon    Ensamblador     1300000
012  |  Laura Quintero      Administrador   2500000
013  |  Viviana Quesada     Guardia         1500000
014  |  Camila Alzate       Ensamblador     2000000
015  |  Leonidas Sanabria   Diseñador       5200000
016  |  Juana Diaz          Ensamblador     1100000
017  |  Laura Playonero     Administrador   2300000
018  |  Viviana Restrepo    Guardia         1400000
019  |  Elias Rodriguez     Ensamblador     1200000
020  |  Mariana Pacheco     Ensamblador     1000000
021  |  Estefany Muñoz      Ensamblador     1900000
022  |  Cristian Fernandez  Ingeniero       3200000
023  |  Jessika Arias       Ensamblador     2100000
024  |  Juan Mendoza        Diseñador       5000000
025  |  Maria Calderon      Ensamblador     1100000
026  |  Laura Lozada        Administrador   2700000
027  |  Yessica Quesada     Guardia         1300000
028  |  Jennifer Alzate     Ensamblador     2100000
029  |  Karen Sanabria      Diseñador       5000000
030  |  Fernando Rodriguez  Ensamblador     1300000
031  |  Nina Londoño        Ensamblador     1200000
032  |  Favio Munera        Ensamblador     1400000
033  |  Lindsey Roy         Ingeniero       3200000
034  |  Nathalia Hernandez  Ensamblador     2100000
035  |  Juan Gaviria        Diseñador       5500000
036  |  Fabio Urrego        Ensamblador     1400000
037  |  Fernanda Quintero   Administrador   2200000
038  |  Camila Queiroz      Guardia         1200000
039  |  Ursula Alzate       Ensamblador     2700000
040  |  Aureliano Buendia   Diseñador       5900000


El ejercicio consiste en almacenar la información en un diccionario llamado empleados (¡OJO!).
Su diccionario debe permitir acceder a la informacion mostrada, utilizando dos indexados. 

Para mayor comprensión, por ejemplo si usted ejecuta estas lineas:
        * empleados["001"]["Cargo"] ===> esta linea retornara "Ingeniero"
        * empleados["005"]["Nombre"] ===> esta linea retornara "Camilo Rodriguez"
        * empleados["016"]["Salario"] ===> esta linea retornara 1100000
        Es decir, en el primer indexado se podrá insertar el codigo (ej: "001", "002", .."018" (strings)),
        en el segundo indexado se podrá indicar la información de interés ("Nombre", "Cargo", "Salario"  (strings))
"""

#------------------------ EJERCICIO 3 --------------------------------
""" El costo de las entradas a cine es el siguiente:
   
                          ----------- 2D ------------        ---------- 3D -------------      
                          ----NIÑO----  ----ADULTO---        ---NIÑO----  ----ADULTO----
 precio (Lunes a viernes)     $5000          $8000              $8000         $12000
 precio (Sabado, domingo)     $7000          $9000              $9000         $15000

Cada una de las ventas de boletas en una semana, se registraron de la siguiente manera:

[
   ("2D_3NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),
   ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
   ("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
   ("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
   ("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")
]

Calcule el numero de boletas vendidas (boletasVendidas) y el dinero recaudado por el cine (dineroRecaudado)

¡OJO! => almacene la respuesta de la siguiente manera:
cine = [boletasVendidas, dineroRecaudado]
"""


#------------------------ EJERCICIO 4 --------------------------------

"""Desarrolle las siguientes funciones: 

NOMBRE DE LA FUNCION     PROBLEMA                                                                                     TIPO DE ENTRADA           RETORNO       
sumaDigitos             * Función que retorne la suma de los digitos de un numero                                    * entero (un numero)     * Entero      
verificadorVocales      * Función que retorne si un mensaje tiene vocales (al menos una) o no                        * Cadena  (un mensaje)   * Booleano    
divisores               * Función que retorne todos los divisores de un numero (no incluir el 1 o el mismo numero)   * Entero  (un numero)    * Lista

¡OJO! => Almacene las funciones de la siguiente manera:
funciones = [sumaDigitos, verificadorVocales, divisores]
"""


#------------------------ EJERCICIO 5 --------------------------------

""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    (el precio de cada seguro es de $120000)

    Para los primeros 30 seguros vendidos, la comisión es del 10%.
    Para los siguientes 100 seguros las comisión es del 35%.
    Para los siguientes seguros vendidos. La comisión es de 15%.

    Realice una funcion llamada calcularSalario (¡OJO!)
    esta función debe tomar como parámetro de entrada el numero de seguros vendidos (int)
    y debe retormar el salario que se le debe pagar al empleado (int)
"""