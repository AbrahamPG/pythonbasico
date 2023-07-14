from final.modulos import funciones


lista = funciones.pedirelementos()
#MOSTRAMOS LISTA SOLICITADA
print("LISTA INGRESADA")
print(lista)
#ELIMINANDO REPETIDOS
print("ELIMINANDO REPETIDOS")
listanueva = funciones.eliminarRepetidos(lista)
#MOSTRANDO LISTA NUEVA SIN REPETIDOS
print(listanueva)
#ORDENANDO EN ASCENDENTE Y DESCENDENTE
print("ORDENANDO")
ordenascendente, ordendescendente = funciones.ordenarlistas(listanueva)
#MOSTRANDO EL ORDEN DE AMBOS CASOS
print("ORDEN ASCENDENTE: ")
print(ordenascendente)
print("ORDEN DESCENDENTE: ")
print(ordendescendente)
#MOSTRAMOS EL MAYOR DE LA LISTA NUEVA, SOLO USAMOS DESPUES DE ORDENARLO
dato = funciones.elementomayor(ordenascendente)
print("MAYOR DE LA LISTA: ")
print(dato)