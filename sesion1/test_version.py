var1 = 20
var2 = 30
var3 = True
var4 = False
resultado = var1 + var2
print(resultado)
print("el valor de mi variable var1 es : {}".format(var1))
print("El valor de mi var3 es : {} y el valor de mi var4 es: {} ".format(var3, var4))

num = float(input("INGRESE UN NUMERO AL AZAR DIFERENTE DE 0: "))
operacion = (num**5)/10
if(operacion%10 == 0) :
    print("EL NUMERO RESULTANTE DESPUES DE HACER LA OPERACION ES ENTERO ")
else   : print(" EL NUMERO ES FLOAT!!!")
