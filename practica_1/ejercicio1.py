#PREGUNTA N°1
lista= []
for i in range (2):
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    print("Su nombre es", nombre, "y tiene", edad, " años")
    lista.append(nombre)
    lista.append(edad)

print(lista)
#suma de edades
suma = lista[1] + lista[3]

print("La suma de las edades de las dos personas es: ", suma)

