def ingresardatos():
    try:
        num1 = input("Ingrese el primer numero: ")
        num2 = input("Ingrese el segundo numero: ")
        print("DATOS INGRESADOS: ", num1," y ",num2, " correctamente!!")
        if isinstance(num1 and num2, str) :
                sumadedatos(num1, num2)
                division(num1, num2)
    except ValueError:
        print("Digite dos datos del mismo tipo!!!!")


def division(num1,num2):
    try:
        if type(num1) == type(num2):
            if isinstance(num1 and num2,str):
                num1 = int(num1)
                num2 = int(num2)
            print("************DIVISION******************")
            print("La division entre los dos numeros es: ",num1/num2)
    except ZeroDivisionError:
        print("no se puede dividir entre 0, cambielos porfavor!!!")
    except TypeError:
        print("Para poder realizar la division")
        print("Los datos tienen que ser del mismo tipo!!!")
def sumadedatos(num1,num2):
    try:
        suma = num1 + num2
        if type(num1) == type(num2):
            print("**************SUMA DE DATOS*****************")
            print("REALIZANDO LA SUMA DE LOS DATOS INGRESADOS:")
    except TypeError:
        print("Digite datos del mismo tipo!!!!")
    else:
        print(suma)

print("Falto tiempo!!!!!")
division(15,12)
sumadedatos(25,"pedro")







#ingresardatos()
