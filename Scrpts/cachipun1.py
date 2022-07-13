import sys
import random
jugador = sys.argv[1].lower()


if (jugador != 'piedra' and jugador != 'papel' and jugador != 'tijeras'):
    print('Argumento inválido: Debe ser piedra, papel o tijera.')
else:
    computador = random.choice(['piedra','papel','tijeras'])

    print(f'''
    Tu jugaste {jugador}.
    Computador jugó  {computador}''')

    if (jugador == 'piedra' and computador == 'tijeras') or (jugador == 'tijeras' and computador == 'papel') or (jugador == 'papel' and computador == 'piedra'):
        print('Felicitaciones has ganado!!!')
    elif jugador == computador:
        print('Empate!!')
    else:
        print('Perdiste :(')
