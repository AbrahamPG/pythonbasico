def ingresar_datos():
    while True:
        try:
            dato1 = int(input("Ingrese el primer dato: "))
            dato2 = int(input("Ingrese el segundo dato: "))
            return dato1, dato2
        except ValueError:
            print("Error: Ingrese solo números enteros.")


def division_entre_cero():
    while True:
        try:
            dato1, dato2 = ingresar_datos()
            resultado = dato1 / dato2
            print(f"La división es: {resultado}")
            break
        except ZeroDivisionError:
            print("Error: División entre cero. Ingrese nuevamente los datos.")


def evaluar_suma_incorrecta():
    while True:
        try:
            dato1, dato2 = ingresar_datos()
            if dato1 + dato2 != 10:
                raise ValueError("La suma es incorrecta.")
            else:
                print("La suma es correcta.")
                break
        except ValueError as e:
            print(f"Error: {str(e)} Ingrese nuevamente los datos.")


# Ejecución del programa
division_entre_cero()
evaluar_suma_incorrecta()
