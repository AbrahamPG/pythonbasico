class Circulo:
    #atributos
    #constructor
    def __init__(self,radio):
        self.radio = radio
        self.resultado = 0

    #metodos
    def area(self):
        #if not isinstance(self.radio, int):
        #    return "El dato no es un entero!!!! "
        if isinstance(self.radio, str ):
            return "El dato no es numerico"
        else:
            resultado = (self.radio**2)*3.14
            return resultado

    def perimetro(self):
        if isinstance(self.radio, str ):
            return "El dato no es numerico"
        else:
            resultado = (self.radio*2)*3.14
            return resultado


circulo1 = Circulo("hola")
circulo2 = Circulo(2)
print("El area del circulo 1 es:", circulo1.area())
print("El perímetro del círculo 2 es:", circulo2.perimetro())
