# Importamos la libreria maath que contiene la funcion ceil.()
import math

# Definición de variables y consultas a usuario
proteina = float(input("Ingrese los gr de protenias: \n"))
carbohidratos = float(input("Ingrese los gr de csrbohidratos \n"))
grasa = float(input(" Ingrese los gr de grasas \n"))

# Proceso
calorias = 4 * (proteina + carbohidratos) + 9 * grasa

# Salida
print(f'Las calorias totales del producto son: {math.ceil(calorias)}')
