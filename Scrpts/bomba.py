# Librerias necesarias para ingresar parametros por conbsola y la funciona time para el control del tiempo
import sys, time

# Fijamos el valor inicial del temporizador
tiempo = int(sys.argv[1]) 

# Ciclo while que nos permite realizar conteo
while tiempo > 0:
    print(tiempo)
    time.sleep(1)
    tiempo -= 1

# Salida que nos permite ver las iteraciones del while
print("Boooom")