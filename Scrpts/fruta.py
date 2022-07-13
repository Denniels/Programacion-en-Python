'''
Un vendedor de frutas necesita calcular el monto que deben pagar sus clientes al
comprar manzanas, cada manzana se vende por unidad y el precio varía según el 
precio puesto por el productor.
Se pide:

a.- Generar un programa que calcule el monto a cancelar para #manzanas vs precio
y que imprima el resultado.

b.- Modificar el programa a.- para que el comerciante pueda ingresar la cantidad 
de manzanas y el precio a través de la terminal.

c.- Modificar el programa b.- y generar un .py que permita ejecutar el programa 
e ingresar los valores de #manzanas y precio por la consola.
'''
from sys import argv
# Metodo para ingresar parametros por consola

manzanas = int(argv[1])
precio = int(argv[2])
total = manzanas * precio

# Metodo para ingresar parametros por terminal
# precio = int(input("Ingrese el valor de las manzanas: "))
# manzanas = int(input("Ingrese la cantidad de manzanas: "))

print(f"La cantidad de manzanas es: {manzanas}\nEl valor unitario es: {precio}\nEl valor total es: {total}")