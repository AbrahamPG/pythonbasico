from datetime import datetime

class Persona:
    nacionalidad = "peruana"
    def __init__(self):
        pass

    def horaregistro(self):
        tiempo = datetime.now()
        hora = tiempo.hour
        minuto = tiempo.minute
        segundo = tiempo.second
        print("Hora de registro: ",hora, ": ", minuto, ": ", segundo )

    def solicitardatos(self):
        try:
            self.nombre = str(input("Ingrese su nombre Porfavor: "))
            self.edad = int(input("Ingrese su edad Porfavor: "))

        except ValueError:
            print("Digite un el tipo de dato que corresponde a lo solicitado!!!!!!")
        else:
            print(self.nombre, "Dato registrado!!!")
            print(self.edad, "Dato registrado!!!")
            self.horaregistro()



    def cumpleanios(self):
        print("Aumentando su edad en 1 año!!!")
        print("Feliz cumpleaños!!!!")
        self.edad = self.edad + 1
        print(self.edad)
    class Sueldo():
        def __init__(self):
            pass
        




#instanciando
person1 = Persona()
#pedimos datos
person1.solicitardatos()
print("***************************************")
print("AUMENTANDO LA EDAD DEL SUJETO EN 2 AÑOS!!")
person1.cumpleanios()
person1.cumpleanios()