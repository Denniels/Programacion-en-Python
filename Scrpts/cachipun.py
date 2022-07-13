'''
Importamos librerias a utilizar sys para pasar argumentos por consola
y random para hacer escojer aleatoramente al pc con random.choice()
'''
import sys, random 

# Definicion de variables y consultas al usuario
sel_usuario = str(sys.argv[1].lower())  # con lower evitamos errores por mayusculas
cachipun = ["piedra", "papel", "tijera"] # nuestra lista tiene strings con minusculas

'''
La seleccion del PC la asignamos con la funcion random.choice(),
la cual se encarga de escoger aleatoriamente un argumento de nuestra lista cachipun
'''
sel_pc =  random.choice(cachipun)

# Presentacion de jugadas
print(f"Tu jugaste {sel_usuario}\nEl computador jugo {sel_pc}")

'''
Esta es la logica de control de flujo del programa, segun la condicion 
que se cumpla se imprime un resultado.
'''

if sel_usuario == "piedra" and sel_pc == "tijera":
    print("!!!Tu ganas")

if sel_usuario == "piedra" and sel_pc == "papel":
    print("Gana el computador") 

if sel_usuario == "papel" and sel_pc == "piedra":
    print("!!!Tu ganas")

if sel_usuario == "papel" and sel_pc == "tijera":
    print("Gana el computador") 

if sel_usuario == "tijera" and sel_pc == "papel":
    print("!!!Tu ganas")

if sel_usuario == "tijera" and sel_pc == "piedra":
    print("Gana el computador")

# Si ambos jugadores seleccionan la misma opcion
if sel_pc == sel_usuario:
    print("!!! Es un empate")

# Si el jugador escoje un argumento no valido
if sel_usuario not in cachipun:
    print(f"Argumento invalido: {sel_usuario}, debes ingresar Piedra Papel o Tijera")