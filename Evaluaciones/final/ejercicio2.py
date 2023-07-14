"""El programa tendrá la función de crear el fichero con el nombre “notas.txt”
crearlo si no existe y el cual será dividido en dos archivos, uno principal
donde se llamará a las funciones que realizarán distintas operaciones en el
otro archivo la cual será llamada funciones.py.
- Crear una función donde se pedirá el tamaño de lista será ingresado por
consola (los números serán llenados de manera aleatoria dentro de la lista),
esta lista será escrita dentro del file “notas.txt”
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.

• Cerrar respectivamente los ficheros cada vez que se abra.
"""
#crearlo si no existe a+
from final.modulos import funciones

funciones.creararchivo()
funciones.pedirtamanolista()
funciones.raizcuadrada()


