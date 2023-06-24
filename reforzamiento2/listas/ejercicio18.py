#Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
#repetidos (los cuales son impares dentro del rango indicado y que no sea el último
#impar).
import sys

lista = []
j= 1
for i in range(15):
    lista.append(j)
    j= j+2

print(lista)
print("agregando 3 numeros: 2 impares y 1 par ")
print("AGREGANDO LOS IMPARES DENTRO DEL RANGO: ", lista[0], " y ", lista[-1], ": ")
numero1 = float(input("DIGITE EL PRIMER NUMERO IMPAR: "))
numero2 = float(input("DIGITE EL SEGUNDO NUMERO IMPAR: "))
#VALIDAMOS SI ES IMPAR
if (numero1 % 2 ==0) or (numero2 %2 ==0) :
    print("Uno de l@s numero(s) introducidos no son impares.......")
    sys.exit()

print("AGREGANDO EL ULTIMO NUMERO SIENDO PAR")
print("AGREGANDO UN NUMERO PAR DENTRO DEL RANGO: ", lista[0], " y ", lista[-1], ": ")
numero3 = float(input("DIGITE EL NUMERO PAR: "))
#VALIDAMOS SI ES PAR O NO
if (numero3 %2 !=0):
    print("El numero ingresado no es par....")
    sys.exit()

#AGREGANDO LOS NUMEROS SOLICITADOS
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
print(lista)

#Agregar un cadena en la posición 3 de la lista.
print("AGREGANDO UN STRING EN LA POSICION 3 ")
lista.insert(2,"HOLA MUNDO")
print(lista)

#Eliminando el string puesto
#con DEL
print("ELIMINANDO EL STRING AÑADIDO ")
del lista[2]
print(lista)

