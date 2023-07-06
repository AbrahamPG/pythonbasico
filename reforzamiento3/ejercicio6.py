class Alumno:
    #atributos

    #constructor
    def __init__(self):
        pass
    #metodos
    def ingresar_nombre(self):
        self.nombre= str(input("Ingrese su nombre porfavor: "))

    def ingresar_edad(self):
        self.edad = int(input("Ingrese su edad porfavor: "))

    def ingresar_nota_final(self):
        self.nota_final = float(input("Ingrese su nota final porfavor: "))

    def mostrar_datos(self):
        print("Nombre(s): ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota final: ", self.nota_final)

    def ifapruebas(self):
        if self.nota_final >= 11:
            print("Felicidades, aprobaste!!!!!")
        else:
            print("Lo lamentamos, desaprobaste :c !!!")

alumno1 = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()

alumno1.ingresar_nombre()
alumno1.ingresar_edad()
alumno1.ingresar_nota_final()
alumno1.mostrar_datos()
alumno1.ifapruebas()

alumno2.ingresar_nombre()
alumno2.ingresar_edad()
alumno2.ingresar_nota_final()
alumno2.mostrar_datos()
alumno2.ifapruebas()

alumno3.ingresar_nombre()
alumno3.ingresar_edad()
alumno3.ingresar_nota_final()
alumno3.mostrar_datos()
alumno2.ifapruebas()


