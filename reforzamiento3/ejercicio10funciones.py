

def ingresarnombres():
    nombre = str(input("Ingrese su nombre: "))
    apellidos = str(input("Ingrese sus apellidos: "))
    print(nombre, " registrado!!!")
    print(apellidos, " registrado!!!")

def pedirseguro():
    seguro = str(input("Ingrese el tipo de seguro que tiene: "))
    print(seguro, " Registrado!!!")
def ifmayor():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Usted es mayor de edad!!!")
    else:
        print("Usted es menor de edad!!!")