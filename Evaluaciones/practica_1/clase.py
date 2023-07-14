nombre = "Abraham Josue"
apellido = "Pacheco Garrido"
fullname = nombre + " " + apellido

condicional = "mayor que " if len(nombre)>len(apellido) else "caracteres de apellido es mayor al de nombres"

print(fullname)
print("tamaño de nombre es: ",len(nombre))
print("tamaño de apellido es: ", len(apellido))
print("nombre completo es: ", fullname.upper())
print(condicional)