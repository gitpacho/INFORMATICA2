"""
Este modulo contiene 3 funciones para imprimir en el juego triqui
"""

def explicarJuego():
    explicacion = """
    ====================================================
    Este es el juego triqui
    
    Es un juego de 2 jugadores, para ganar debe 
    completar 3 caracteres iguales en linea ("x" o "o")
    
    Para ingresar la posicion en el juego, guiese
    con los siguientes numeros

                0  | 1 |  2
                ------------- 
                3  | 4 |  5
                ------------- 
                6  | 7 |  8

    =====================================================
    """
    print(explicacion)

tableroLista = ["x", "o", None, None,None,None,None,None,None]

def dibujarTablero(tableroLogico:list):
    tableroVisual = """
                {}  | {} |  {}
                ------------- 
                {}  | {} |  {}
                ------------- 
                {}  | {} |  {}
    """.format(tableroLogico[0], tableroLogico[1],
               tableroLogico[2], tableroLogico[3],
               tableroLogico[4], tableroLogico[5],
               tableroLogico[6], tableroLogico[7],
               tableroLogico[8])

    print(tableroVisual)


if __name__ == "__main__":
    explicarJuego()
    tablero = [None]*9
    dibujarTablero(tablero)