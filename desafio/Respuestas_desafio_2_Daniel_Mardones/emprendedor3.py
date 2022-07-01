'''
Siempre se utiliza la siguiente formula
    Utilidades = P * U - GT
3. Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior, todo esto mediante input(). 
El programa debe calcular las utilidades actuales y mostrar la razón entre 
las utilidades actuales y las del año anterior con dos decimales.
(2 Puntos)
'''

# Definición de variables y consultas a usuario
precio_suscripcion = int(input("Ingrese el valor de la suscripción: "))
numero_usuarios = int(input("Ingrese el número del usuario: "))
gastos_totales = int(input("Ingrese los gastos totales: "))
utilidades_pasado = int(input("Ingrese las utilidades del año anterior: "))

# Proceso
utilidad = (precio_suscripcion * numero_usuarios) - gastos_totales
razon = utilidades_pasado / utilidad
# Variable con funcion round para calibrar la salida esperada
razon_decimales = round(razon, 2)

# Salida
print(f"La utilidad actual es {utilidad}")
print(f"La razón de la utilidad actual con la del año anterior es: {razon_decimales}")