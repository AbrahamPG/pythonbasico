#Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())
lista = [ 1, 2 ,3 ,15.6, 12.5, 36.8, True, False ]
print("IMPRIMIENDO LOS DOS ULTIMOS SIN SABER LA CANTIDAD DE ELEMENTOS: ")
print(lista[-2:len(lista)])
print("AHORA VEREMOS QUE TIPO DE ELEMENTOS SON CADA UNO: ")
j=0
for i in range(len(lista)) :
    print("ELEMENTO ", j , "es de: ")
    print(type(lista[i]))
    j=j+1

