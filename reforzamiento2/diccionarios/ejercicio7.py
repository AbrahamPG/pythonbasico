#Crear un diccionario con 6 departamentos en el país.
#Borrar cualquier departamento (uno) usando la palabra reservada del.
#Comprobar que no existe este departamento borrado dentro del diccionario.

diccionario = {"Lima":"Lima",
               "Loreto": "Iquitos",
               "Madre de Dios":"Puerto Maldonado",
               "Cusco": "Cusco",
               "Puno":"Puno",
               "Moquegua":"Moquegua"}

print(diccionario)

del diccionario["Lima"]
print(diccionario)
print("BUSCANDO EL DEPARTAMENTO ELIMINADO...")
print(diccionario.get("Lima","No existe un departamento con ese nombre....."))
print("AÑADIENDO NUEVO VALOR EN VEZ DE UNA CAPITAL: ")
#diccionario["Moquegua"] = "Ingenieria de software"
diccionario.update({"Moquegua": "Ingenieria de software"})
print(diccionario)