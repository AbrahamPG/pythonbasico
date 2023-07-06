class Cadena:
    #atributos
    #constructor: valor por defecto
    def __init__(self, cadena):
        self.cadena = cadena

    def revertir(self):
        palabra = self.cadena.split()
        cadena_revertida = palabra[::-1]
        self.cadena = " ".join(cadena_revertida)



#iniciando una instancia

cadena1 = Cadena("Hola pythonista, seguimos adelante")

print("cadena ingresado: ", cadena1.cadena)
cadena1.revertir()
print("cadena : ", cadena1.cadena)
print("llamando de nuevo a la funcion.....")
cadena1.revertir()
print("cadena : ", cadena1.cadena)

