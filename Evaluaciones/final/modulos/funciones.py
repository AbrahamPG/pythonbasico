import random
import math

def pedirelementos():
    lista=[]
    for i in range (0,10):
        dato = input(f"Digite el elemento n°{i+1} de la lista: ")
        lista.append(dato)
    return lista

def eliminarRepetidos(lista):
    numerosnorepetidos = (set(lista))
    lista_enteros = [int(x) for x in numerosnorepetidos]
    return lista_enteros

def ordenarlistas(lista):
    menormayor = sorted(lista)
    mayormenor = sorted(lista,reverse=True)
    return menormayor , mayormenor

def elementomayor(lista):
    return lista[-1]




"""ARCHIVO/LISTAS"""

def creararchivo():
    open("myfiles/notas.txt", "a+")

def pedirtamanolista():
    tamano = int(input("Ingrese el tamaño de la lista: "))
    lista = [random.randint(1,100) for i in range(tamano)]
    #PARTE DE ARCHIVOS
    file = open("myfiles/notas.txt", "w")
    file.write("Lista de numeros: \n")
    for numero in lista:
        file.write(str(numero) + "\n")

def raizcuadrada():
    file = open("myfiles/notas.txt", "a")
    file.write("La raiz cuadrada de los elementos son: \n")
    with open('myfiles/notas.txt', 'r') as archivo_lectura:
        lineas = archivo_lectura.readlines()
        for linea in lineas[1:]:
            #convertimos a entero los strings mandados desde la linea 2 lineas[0:] 0: primeralinea    1: se refiere desde segunda linea
            numero = int(linea.strip())
            raiz_cuadrada = math.sqrt(numero)
            file.write(str(raiz_cuadrada) + '\n')




