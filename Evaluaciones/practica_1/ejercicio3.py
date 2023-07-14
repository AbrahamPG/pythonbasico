diccionario = {}


# Solicitar al usuario que ingrese los pares clave-valor
for i in range(4):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario[clave] = valor

# Mostrar el diccionario
print("Diccionario:", diccionario)

#eliminando una clave
print("\nELIMINANDO EL DNI")
diccionario.pop("dni")
print("Diccionario:", diccionario)

# Pedir al usuario que ingrese la nueva clave y su valor
print("\nAGREGANDO NUEVA CLAVE Y VALOR")
nueva_clave = input("Ingrese la nueva clave: ")
nuevo_valor = input("Ingrese el valor para la nueva clave: ")

# Agregar la nueva clave y valor al diccionario
diccionario[nueva_clave] = nuevo_valor

# Mostrar el diccionario actualizado
print("Diccionario:", diccionario)

