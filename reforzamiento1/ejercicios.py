"""EJERCICIO NUMERO 1"""
print("EJERCICIO NUMERO 1: ")
nombre = "Abraham Josue"
mi_saludo = "¡Hi " + nombre + "!"
print(mi_saludo)

"""EJERCICIO NUMERO 2"""
print("\nEJERCICIO NUMERO 2: ")
num = 53
print(num*10 - 10)

"""EJERCICIO NUMERO 3"""
print("\nEJERCICIO NUMERO 3: ")
var = "536"
num = 25
suma = int(var) + num
print(suma)

"""EJERCICIO NUMERO 4"""
print("\nEJERCICIO NUMERO 4: ")
pi= 3.14
radio = float(input("Ingrese el radio de la esfera: "))
volumen= (4/3)*pi*(radio**3)
print("El volumen de la esfera es: " , volumen )

"""EJERCICIO NUMERO 5"""
print("\nEJERCICIO NUMERO 5: ")
numero = float(input("Ingrese su sueldo: "))
if(numero%2 == 0) :
    print("Su sueldo es un numero par!!!!")
else : print("Su sueldo es un numero impar!!!")

"""EJERCICIO NUMERO 6"""
print("\nEJERCICIO NUMERO 6: ")
num1 = 12.2
num2 = 12.9
num3 = 15.7
num4 = 16.4
num5 = 20.9
media = (num1 + num2 + num3 + num4 + num5)/5
print("LA MEDIA DE LOS 5 NUMEROS ES ", media)

"""EJERCICIO NUMERO 7"""
print("\nEJERCICIO NUMERO 7: ")
a = 50
b = 60
c = 87
resultado = (a%3) + (b%5) + (c%7)
print(" LA SUMA DE LOS MODULOS CON 3, 5 Y 7 RESPECTIVAMENTE")
print(" es: ", resultado)

"""EJERCICIO NUMERO 8"""
print("\nEJERCICIO NUMERO 8: ")
lista1 = []
lista2 = [1,2,3,4,5,6]
print("Lista 1 ")
if(len(lista1) == 0 ):
    print("La lista esta vacia!!!")
else  : print("La lista contiene datos!!!")
print("LISTA 2 ")
if(len(lista2) == 0 ):
    print("La lista esta vacia!!!")
else  : print("La lista contiene datos!!!")

"""EJERCICIO NUMERO 9"""
print("\nEJERCICIO NUMERO 9: ")
num = float(input("Ingrese un numero: "))
resultado= (pow(num,4)) - num*2
print("EL RESULTADO ES : " , resultado)

"""EJERCICIO NUMERO 10"""
print("\nEJERCICIO NUMERO 10: ")
# Crear el diccionario
datos_personales = {
    "nombre": "Abraham",
    "carrera": "Ingeniería Informática",
    "edad": 25,
    "año de nacimiento": 1997
}
# Mostrar los valores del diccionario
print(datos_personales)

"""EJERCICIO NUMERO 11"""
print("EJERCICIO NUMERO 11: ")
num = float(input("\nINGRESE UN NUMERO AL AZAR DIFERENTE DE 0: "))
operacion = (num**5)/10
if(operacion%10 == 0) :
    print("EL NUMERO RESULTANTE DESPUES DE HACER LA OPERACION ES ENTERO ")
else   : print(" EL NUMERO ES FLOAT!!!")





