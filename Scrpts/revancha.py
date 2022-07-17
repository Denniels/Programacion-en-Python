import random
# pool de números
pool_loto = [n for n in range(1,42)]

pool_revancha = [n for n in range(1,42)]

# la posición de extracción
posiciones = ['primer número',
              'segundo número',
              'tercer número',
              'cuarto número',
              'quinto número',
              'sexto número',
              'comodín']

def sacar_numero(posicion, sorteo):
    if sorteo == 'Loto':
        global pool_loto
        elegido = random.choice(pool_loto)
        pool_loto.remove(elegido)
    else:
        global pool_revancha
        elegido = random.choice(pool_revancha)
        pool_revancha.remove(elegido)

    print(f'{sorteo}: El {posicion} es {elegido}')

def sortear(sorteo, posiciones = posiciones):
    if sorteo == 'Revancha':
        posiciones = posiciones[:-1]

    for pos in posiciones:
        sacar_numero(pos, sorteo)

eleccion = input('''Bienvenidos. ¿Qué desea jugar?
                 1. Loto
                 2. Loto + Revancha
                 > ''')

# Elección de Sorteos
if eleccion == '1':
    sortear('Loto')

elif eleccion == '2':
    sortear('Loto')
    sortear('Revancha')
else:
    print('Elección no válida')
    
print('Sorteo Terminado')