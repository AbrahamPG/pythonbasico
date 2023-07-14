import time

"""
Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo, multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados con un mínimo tres ejemplos.
"""
def medir_tiempo(funcion):
    def interna(**kwargs):
        start_time = time.time()
        result = funcion(**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        #tiempo muy corto ya que lo ejecuta demasiado rapido
        print(f"Tiempo de ejecución de {funcion.__name__}: {execution_time} segundos")
        return result
    return interna

@medir_tiempo
def multiplicacion(**kwargs):
    resultado = 1
    for key, value in kwargs.items():
        resultado *= value
    return resultado

# Ejemplos
resultado1 = multiplicacion(a=2, b=3, c=4)
print("Resultado 1 de la multiplicacion: ", resultado1)

resultado2 = multiplicacion(x=5, y=2)
print("Resultado 2 de la multiplicacion: ", resultado2)

resultado3 = multiplicacion(p=3, q=7, r=2, s=4, t=10)
print("Resultado 3 de la multiplicacion: ", resultado3)
