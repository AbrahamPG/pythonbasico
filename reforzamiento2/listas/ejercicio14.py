#Elimina un elemento por dos índices existentes y ya no por el valor.
import sys

lista = [ 1, 2 ,3 ,15.6, 12.5, 36.8, True, False ]

print("ESCOJA DOS INDICES DEL 1 AL 8: ")
indice1 = int(input("INDICE UNO: "))
indice2 = int(input("INDICE DOS: "))
if(indice1 and indice2) not in range(1-8):
    print("UNO DE LOS DIGITOS NO ESTAN EN EL RANGO DE 1 A 8")
    sys.exit()
lista.pop(indice1)
print(lista)
lista.pop(indice2)
print(lista)

