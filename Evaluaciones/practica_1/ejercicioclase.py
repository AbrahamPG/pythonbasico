datos = input("ingrese sus nombres y apellidos: ")

lista = datos.split()
apellidos = lista[-2 ] + " " + lista[-1]


#output
print("Los apellidos son : " , apellidos)
