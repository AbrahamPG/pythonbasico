class Numero:
    """atributos"""

    """constructor: valores por defecto"""

    def __init__(self ,numero):
        self.numero = numero

    """metodos: """
    def elevar_cuadrado(self):
        self.numero = (self.numero)**2
        return self.numero


#INSTANCIANDO NUESTRA CLASE
num1 = Numero(5)
print("numero: ", num1.numero)
print("ELEVANDO EL NUMERO AL CUADRADO RESULTA: ", num1.elevar_cuadrado())
print("numero actual es: ", num1.numero)