"""Ejercicio:
    2) Crear una clase llamada Decimal
       con un unico atributo: valorNumerico
       con los metodos convertirABinario, conventirAOctal, convertirAHexadecimal,  """


class Decimal:
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico

    def convertirABinario(self):
        conversion = bin(self.valorNumerico)
        return conversion
        
    def conventirAOctal(self):
        conversion = oct(self.valorNumerico)
        return conversion

    def convertirAHexadecimal(self):
        conversion = hex(self.valorNumerico)
        return conversion
