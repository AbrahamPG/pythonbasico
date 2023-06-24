#Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media
#de los números.

print("INGRESE 10 NUMEROS EN LA SIGUIENTE LISTA: ")
lista = [None]*10
print(len(lista))
#sum = 0
for i in range(10):
    lista[i] = int(input("Ingrese el valor #" + str(i + 1) + ": "))
    #sum = sum + lista[i]

#
sum = sum(lista)
prom = sum/10
print("LA SUMA DE LOS NUMEROS ES: ", sum)
print("EL PROMEDIO DE LOS NUMEROS ES: ", prom)
