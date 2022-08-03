from html_module import create_html_earth
from html_module import create_html_planet
from html_module import create_html_pic
from show import show_pic
from validar import validate
from apod import pull_fotos
from planet import pull_planetas
from earth import pull_earth
import data as d
import time
import os
import sys

clear = 'cls' if sys.platform == 'win32' else 'clear'


while True:
    os.system(clear)
    opcion = input(d.MENU)
    opcion = int(validate(['0', '1', '2', '3'], opcion))

    if opcion == 1:
        os.system(clear)
        n = int(input(d.APOD))
        print('Estamos procesando tus fotos...')
        id_foto = pull_fotos(n)
        html = create_html_pic(id_foto)
        show_pic(html, 'apod')
        time.sleep(3)

    elif opcion == 2:
        os.system(clear)
        planeta = input(d.PLANETA)
        planeta = int(validate(['1', '2', '3', '4', '5', '6', '7', '8'], planeta))
        n = int(input('Cuantas fotos quieres ver '))
        print('Estamos procesando tus fotos...')
        titulos, descripcion, fotos = pull_planetas(planeta, n)
        html = create_html_planet(titulos, descripcion, fotos)
        show_pic(html, 'planetas')
        time.sleep(3)

    elif opcion == 3:
        os.system(clear)
        fecha = input(d.TIERRA)
        fotos, horas = pull_earth(fecha)
        html = create_html_earth(fotos, horas)
        show_pic(html, 'tierra')
        time.sleep(3)

    else:
        print('Gracias por venir')
        time.sleep(2)
        exit()