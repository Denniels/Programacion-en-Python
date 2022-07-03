'''
Siempre se utiliza la siguiente formula
    Utilidades = P * U - GT
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
(3 Puntos)

'''
# Definición de variables y consultas a usuario
precio_suscripcion = int(input("Ingrese el valor de la suscripción: "))
tipo_usuario = str(input("Ingrese Unormal o Upremium: "))
numero_usuario = int(input("Ingrese el numero de usuario: "))
gastos_totales = int(input("Ingrese los gastos totales: "))

# Variable que aumenta el valor de la subcripción
extra = precio_suscripcion + ((precio_suscripcion * 50)/100)
utilidad = 0

# Proceso
if tipo_usuario == str("Unormal"):
    utilidad = (precio_suscripcion * numero_usuario) - gastos_totales

# Salida para usuarios normales
    print(utilidad)

if tipo_usuario == str("Upremium"):
    utilidad = (extra * numero_usuario) - gastos_totales

# Salida para usuarios premium
    print(utilidad)