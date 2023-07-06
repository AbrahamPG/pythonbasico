class Agenda:
    #atributos
    #constructor
    def __init__(self,lista):
        #self.lista = lista
        pass
    #metodos
    def aniadircontacto(self):
        self.lista=[]
        self.diccionario = {"nombre": "none", "telefono": "none", "e-mail": "none", "dni": "none"}
        self.diccionario["nombre"] = str(input("Ingrese el nombre: "))
        self.diccionario["telefono"] = str(input("Ingrese el telefono: "))
        self.diccionario["e-mail"] = str(input("Ingrese su correo: "))
        self.diccionario["dni"] = int(input("Ingrese el dni: "))
        self.lista.append(self.diccionario)
        print("Usuario registrado.....")

    def mostrarcontactos(self):
        print("Mostrando contactos....")
        print(self.lista)

    def buscarcontacto(self):
        print("Buscando Contacto por DNI!!!")
        valor = input("Digite el dni a buscar: ")
        for self.diccionario in self.lista:
            if valor in self.diccionario.values():
                print("El valor ", valor, "pertenece al usuario: ", self.diccionario)
                break
            else:
                print("No se encontro el valor ", valor, " en ninguno de los diccionarios!!")
agenda1 = Agenda([])
agenda1.aniadircontacto()
print("..........................................")
agenda1.mostrarcontactos()
print("..........................................")
agenda1.buscarcontacto()
print("..........................................")