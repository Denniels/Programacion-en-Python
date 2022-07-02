import sys  # Librería que contiene la función sys.argv, para ingresar parámetros por consola.
'''
Se le debe indicar el tipo de dato que
vamos a ingresar por consola, por ello
usamos float para agregar la variable a
los argumentos.
El orden de ingreso de los argumentos son los siguientes:
°1 sol, °2 peso argentino, °3 dólar, °4 pesos chilenos a convertir
'''
# Variables
sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])
peso_chileno = float(sys.argv[4]) # Se usa float por si alguien ingresa un valor con decimales
# peso_chileno = int(sys.argv[4]) # Si solo se van ingresar valores enteros se puede des comentar esta línea y comentar la línea 14

# Presentación
print("----------------------")
print("Conversión de divisas")
print("----------------------")

# Proceso de conversion de divisas
resultado_1 = peso_chileno * sol
resultado_2 = peso_chileno * peso_argentino
resultado_3 = peso_chileno * dolar

# Salida de resultados
print(f"Los {peso_chileno} pesos Chilenos equivalen a:\n{resultado_1} Soles\n{resultado_2} Pesos Argentinos\n{resultado_3} Dólares")
#print("Los {} pesos Chilenos equivalen a:\n{} Soles\n{} Pesos Argentinos\n{} Dolares".format(peso_chileno, resultado_1, resultado_2, resultado_3))