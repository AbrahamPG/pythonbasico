class Persona:
    #atributos
    #constructor
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    #metodos
    #vacio
    class Empleado:
        #atributos
        #constructor
        def __init__(self):
            super().__init__()
            self.sueldo = int(input("Ingrese el sueldo: "))
        #metodos
        def ifpaga(self):
            if (self.sueldo > 4000):
                impuesto = self.sueldo*0.1
                print("Usted paga impuestos!!!")
                print("La cantidad a pagar por impuestos es de: ",impuesto)
            else:
                print("Usted no paga impuestos...")

        def mostrarsueldo(self):
            print("Su sueldo es de: ", self.sueldo)


nombre = str(input("Ingrese el nombre de la persona: "))
edad = int(input("Ingrese la edad de la persona: "))
empleado1 = Persona(nombre,edad).Empleado()
print(empleado1.mostrarsueldo())
print(empleado1.ifpaga())
