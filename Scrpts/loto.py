import random

pool = [n for n in range(1, 42)]

posiciones = ['Primer numero', 
              'Segundo numero', 
              'Tercer numero', 
              'Cuarto numero', 
              'Quinto numero', 
              'Sexto numero', 
              'Comodin']

def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')

for posicion in posiciones:
    sacar_numero(posicion)
    print(pool)

print('El sorteo a finalizado')



'''
Todo esto se resume con la funcion de arriba
# Numero 1
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# Numero 2
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# Numero 3
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# Numero 4
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# Numero 5
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# Numero 6
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero elegido es: ', elegido)

# numero 7 o comodin
elegido = random.choice(pool)
pool.remove(elegido)
print('El numero comodin es: ', elegido)
'''