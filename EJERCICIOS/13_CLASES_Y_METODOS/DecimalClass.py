"""Ejercicio:
    2) Crear una clase llamada Decimal
       con un unico atributo: valorNumerico
       con los metodos convertirABinario, conventirAOctal, convertirAHexadecimal,  """


class Decimal:
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico

    def convertirABinario(self):
        conversion = bin(self.valorNumerico)
        return conversion[2:]
        
    def conventirAOctal(self):
        conversion = oct(self.valorNumerico)
        return conversion[2:]

    def convertirAHexadecimal(self):
        conversion = hex(self.valorNumerico)
        return conversion[2:]

if __name__ == "__main__":
    decimal1 = Decimal(8)
    decimal2 = Decimal(15)
    print("Decimal 8")
    print(decimal1.convertirABinario())
    print(decimal1.conventirAOctal())
    print(decimal1.convertirAHexadecimal())

    print("Decimal 15")
    print(decimal2.convertirABinario())
    print(decimal2.conventirAOctal())
    print(decimal2.convertirAHexadecimal())



"""
crear las clases Octal, Hexadecimal y Binario
e incluya los metodos necesarios para realizar las conversiones
a los otros sistemas numericos
"""







