'''
El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:

                IMC = W / H2
donde:
W : corresponde al peso de la persona en Kg.
H: corresponde a la altura en metros.
IMC: EL valor del IMC, en [Kg/m2]
'''

# Librería que contiene la función sys.argv, para ingresar parámetros por consola.
import sys 

# Definición de variables
peso = float(sys.argv[1])
altura = float(sys.argv[2])

# Lista con las información de las clasificaciones de la OMS
clas_peso = ["Bajo peso", "Adecuado", "Sobrepeso", 
             "Obesidad gardo 1", "Obesidad grado 2", 
             "Obesidad grado 3"]

# Lista con los pesos de las clasificaciones
clas_kilos = [18.5, 25, 30, 35, 40]

# Cálculo IMC
imc = peso / (altura/100)**2

# Salida del calculo IMC
print(f"Su IMC es: {imc:.2f}")

'''
La salida de la clasificación OMS, se imprime si se cumplen 
las siguientes condiciones de control de flujo, usamos los índices
para acceder a cada lista y comparamos lo valores si son mayores o menores 
que el resultado de IMC, con esto según el IMC y las comparaciones 
obtenemos una salida.
'''
if imc <= clas_kilos[0]:
    print(f"Su clasificacion OMS es: {clas_peso[0]}")

if imc > clas_kilos[0] and imc < clas_kilos[1]:
    print(f"Su clasificacion OMS es: {clas_peso[1]}")

if imc > clas_kilos[1] and imc < clas_kilos[2]:
    print(f"Su clasificacion OMS es: {clas_peso[2]}")

if imc > clas_kilos[2] and imc < clas_kilos[3]:
    print(f"Su clasificacion OMS es: {clas_peso[3]}")

if imc > clas_kilos[3] and imc < clas_kilos[4]:
    print(f"Su clasificacion OMS es: {clas_peso[4]}")

if imc > clas_kilos[4]:
    print(f"Su clasificacion OMS es: {clas_peso[5]}")