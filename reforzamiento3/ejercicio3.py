class Diccionario:
    #atributos
    #constructor
    def __init__(self):
        pass

    #metodos

    def dato1(self):

        self.nombres = input("Ingresar sus nombres: ")
        self.apellidos = input("Ingresar sus apellidos: ")

    def dato2(self):
        self.edad = input("Ingresa tu edad: ")

    def impresion(self):
        mostrar = {}
        mostrar["nombres"] = self.nombres
        mostrar["apellidos"] = self.apellidos
        mostrar["edad"] = self.edad
        print(mostrar)


#INSTANCIANDO
diccionario = Diccionario()
diccionario.dato1()
diccionario.dato2()
diccionario.impresion()
