#Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el resultado en
#consola. (Pista: len(lista))
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
