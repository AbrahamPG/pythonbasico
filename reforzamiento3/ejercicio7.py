class Persona:
    #atributos
    #constructor
    def __init__(self):
        pass
    #metodos
    def ingresar_nombre(self):
        self.nombre= str(input("Ingrese su nombre porfavor: "))

    def ingresar_edad(self):
        self.edad = int(input("Ingrese su edad porfavor: "))

    def ingresar_sueldo(self):
        self.sueldo = float(input("Ingrese su sueldo porfavor: "))

    def bonificacion(self):
        print("Usted cuenta con: ", (self.sueldo) * 0.2, " de bonificacion")
        print("Total recibido: ", (self.sueldo) * 1.2)

    def mostrar_datos(self):
        print("Nombre(s): ", self.nombre)
        print("Edad: ", self.edad)
        print("Sueldo: ", self.sueldo)

        if self.edad >= 18:
            print("Persona mayor de edad!!!!!")
        else:
            print("Persona menor de edad!!!!!")

        #print("Usted cuenta con: ", (self.sueldo)*0.2 , " de bonificacion")
        #print("Total recibido: ", (self.sueldo)*1.2)
        self.bonificacion()




persona1 = Persona()
persona2 = Persona()

persona1.ingresar_nombre()
persona1.ingresar_edad()
persona1.ingresar_sueldo()
persona1.mostrar_datos()

persona2.ingresar_nombre()
persona2.ingresar_edad()
persona2.ingresar_sueldo()
persona2.mostrar_datos()