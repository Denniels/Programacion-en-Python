import math

proteina = float(input("Ingrese los gr de protenias: \n"))
carbohidratos = float(input("Ingrese los gr de csrbohidratos \n"))
grasa = float(input(" Ingrese los gr de grasas \n"))

calorias = 4 * (proteina + carbohidratos) + 9 * grasa

print(f'Las calorias totales del producto son: {math.ceil(calorias)}')
