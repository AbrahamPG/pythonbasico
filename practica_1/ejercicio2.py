import random


lista = []

for i in range (10):
    numero = random.randint(0, 8)
    lista.append(numero)
print("LISTA NORMAL: ")
print(lista)
cubos = []
#ELEVAREMOS CADA ELEMENTO AL CUBO

for i in range(10):
    i = lista[i]**3
    cubos.append(i)
print("EL CUBO DE LA LISTA: ")
print(cubos)

#LISTAS INVERSAS
lista.reverse()
cubos.reverse()
print("EL INVERSO DE LAS DOS LISTAS: ")
print(lista)
print(cubos)
sumalistas = []

for i in range(10):
    i = (lista[i] + cubos[i])
    sumalistas.append(i)
print("LA SUMA DE LOS INVERSOS: ")
print(sumalistas)





