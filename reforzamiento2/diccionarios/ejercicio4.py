#Elimina el key edad tipo de tu diccionario, incluyendo su valor.

diccionario = {"nombre": "Abraham", "edad": 25, "salario": 1550}
print(diccionario)

diccionario["dni"] = "74096065"
print(diccionario)

#diccionario.pop("edad")
#print(diccionario)

del diccionario["edad"]
print(diccionario)