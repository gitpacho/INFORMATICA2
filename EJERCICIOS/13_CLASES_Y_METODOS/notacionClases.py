# 08-11-2022

"""
Crear una clase llamada ComidaColombiana
atributos: ingrediente1, ingrediente2, ingrediente3
metodos: nutrir y provocar
"""

class ComidaColombiana:
    #Para crear los atributos
    def __init__(self, ingrediente1,ingrediente2, ingrediente3):
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.ingrediente3 = ingrediente3
    
    #Para crear metodos (funciones)
    def provocar(self, opcion):
        if opcion in ["huele bien", "se ve bien", "tengo hambre"]:
            return "Este alimento provoca"
        else:
            return "Este alimento no provoca"

    def nutrir(self, opcion):
        if opcion in ["estoy enfermo", "tengo nauseas", "el doctor me prohibio"]:
            return "Este almiento no me puede nutrir"
        else:
            return "Este alimento me nutre"


#Como creo el objeto ?
bandejaPaisa = ComidaColombiana("chorizo", "arepa", "chicharron")
sancochoDeGallina = ComidaColombiana("gallina", "papa", "caldo")
ajiacoSantafereño = ComidaColombiana("papa", "pollo", "aguacate")
print("Es instancia? =>", isinstance(ajiacoSantafereño, ComidaColombiana))

#Cómo accedo a los atributos de un objeto
atributoA = bandejaPaisa.ingrediente3
atributoB = sancochoDeGallina.ingrediente1
atributoC = ajiacoSantafereño.ingrediente2
print("atributos =>", atributoA, atributoB, atributoC)


#Cómo acceder a los métodos de un objeto


print(ComidaColombiana.__dict__)