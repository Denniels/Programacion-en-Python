'''
     Utilidades = P * U - GT
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

Para ello, se te pide desarrollar este cálculo en tres versiones:
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto. 
Para ello utiliza input() para solicitar como dato el precio de 
suscripción P, el número de usuarios U y el gasto total GT. (5 Puntos)
'''
# Definición de variables y consultas a usuario
precio_suscripcion = int(input("Ingrese el valor de la suscripción: "))
numero_usuarios = int(input("Ingrese el número del usuario: "))
gastos_totales = int(input("Ingrese los gastos totales: "))

# Proceso
utilidad = (precio_suscripcion * numero_usuarios) - gastos_totales

# Salida
print(utilidad)