import random

def elegir_tv(eleccion):
    peliculas = ['Scarface', 'Crepúsculo', 'Up']
    series = ['Dark', 'Friends', 'El Reemplazante']
    if eleccion == '1':
        print(f'Te recomiendo ver {random.choice(peliculas)}')
    elif eleccion == '2':
        print(f'Te recomiendo ver {random.choice(series)}')
    else:
        print(f'Ingresaste una opción inválida. No puedo recomendar nada.')

def elegir_cocina(eleccion):
    comidas = ['Filete Mignon', 'Cazuela', 'Bistec a lo Pobre']
    postres = ['Creme Brulee', 'Macedonia', 'Tiramisú']
    if eleccion == '1':
        print(f'Te recomiendo cocinar {random.choice(comidas)}')
    elif eleccion == '2':
        print(f'Te recomiendo cocinar {random.choice(postres)}')
    else:
        print(f'Ingresaste una opción inválida. No puedo recomendar nada.')

def submenu(eleccion):
    if eleccion == '1':
        texto = '''Elige entre:
                1. Comidas
                2. Postres
                > '''
    else:
        texto = '''Elige entre:
                1. Películas
                2. Series
                > '''
    return input(texto)

opcion = input('''¿Estás aburrido? ¿Qué quieres hacer?
                1. Cocinar
                2. Ver Televisión
                > ''')
opcion2 = submenu(opcion)
if opcion == '1':
    elegir_cocina(opcion2)
elif opcion == '2':
    elegir_tv(opcion2)