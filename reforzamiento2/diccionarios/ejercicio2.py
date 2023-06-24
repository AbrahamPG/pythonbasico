#Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola.

diccionario = {"nombre": "Abraham", "edad": 25, "salario": 1550}
print(diccionario)

#    Posible solucion #1
lista = list(diccionario.items())
print("LA LISTA QUEDARIA ASI: ", lista)
for i in range(len(lista)) :
    print("El tipo de dato de la posicion ", i , "es: ", type(lista[i]))

#    Posible solucion #2
lista1 = list(diccionario)
print("LA LISTA QUEDARIA ASI: ",lista1)
for i in range(len(lista1)) :
    print("El tipo de dato de la posicion ", i , "es: ", type(lista1[i]))

#    Posible solucion #3
lista2=[]
for valor1 , valor2 in diccionario.items():
    lista2.append(valor1)
    lista2.append(valor2)
print("LA LISTA QUEDARIA ASI: ",lista2)
for i in range(len(lista2)) :
    print("El tipo de dato de la posicion ", i , "es: ", type(lista2[i]))


