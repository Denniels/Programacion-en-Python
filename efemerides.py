efemerides = {'1 de enero':'Año nuevo',
              '27 de febrero':'Terremoto en chile',
              '8 de marzo':'Dia de la Mujer',
              '21 de mayo':'Glorias Navales',
              '18 de septiembre':'Fiestas Patrias',
              '19 de septiembre':'Glorias del Ejercito',
              '25 de diciembre':'Navidad'}

fecha = input("Ingrese una fecha: ").lower()

print(f'Efemerides: {efemerides.get(fecha, "No hay eventos para esta fecha")}')