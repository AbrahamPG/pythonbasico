#Borra el primer ítem de la lista usando debidamente su índice.
lista = ["diseño de software","metodos numericos", "arquitectura de software", "economia", "base de datos", "oratoria"]
print(lista)

lista.append("fisica")
lista.append("quimica")
lista.append("datawarehouse")
lista.append("taller de software")
print(lista)

lista.remove("diseño de software")
lista.remove("arquitectura de software")
print(lista)

lista.reverse()
print(lista)

cantidadlista = len(lista)
print(cantidadlista)

lista.append("fisica")
lista.append("fisica")
lista.append("oratoria2")
lista.append("diseño de software")
print("La cantidad de veces que se repite el curso fisica es de: ",lista.count("fisica") )

print(lista)
lista.pop(0)
print(lista)