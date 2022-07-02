# Creamos diccionario con las fechas de las efemerides
efemerides = {'1 de enero':'Año nuevo',
              '27 de febrero':'Terremoto en chile',
              '8 de marzo':'Dia de la Mujer',
              '21 de mayo':'Glorias Navales',
              '18 de septiembre':'Fiestas Patrias',
              '19 de septiembre':'Glorias del Ejercito',
              '25 de diciembre':'Navidad'}

'''
Definición de variable y consultas a usuario,
usamos la funcion lower para evitar errores de tipeo,
asi buscamos solo letras minusculas
'''
fecha = input("Ingrese una fecha: ").lower()

# Salida, y si no hay coincidencias imprime un mensaje
print(f'Efemerides: {efemerides.get(fecha, "No hay eventos para esta fecha")}')