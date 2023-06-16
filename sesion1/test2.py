"""jiijji"""
""" CREAR 3 VARIABLES: 
- nombre, apellido, edad y sueldo(float)
-Imprimir el siguiente mensaje " Hola nombre apellido, su sueldo actual 
es de : sueldo soles"
-Mostrar la suma (concatenacion) del sueldo y la edad en un mensaje 
"""


nombre = "Abraham"
apellido = "Pacheco"
edad= "25"
sueldo = 1559.6

print("Hola {}  {}, su sueldo actual es de : {} soles".format(nombre, apellido, sueldo))
Suma = sueldo + int(edad)
print("La suma de la edad y el sueldo es : {}".format(Suma))