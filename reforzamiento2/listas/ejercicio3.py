#Quita 2 elementos de tu nueva lista ítems por valor, no por índice.

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


