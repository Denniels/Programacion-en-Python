import sys

# Libreria contenedora de argv para pasar parametros por consola
import sys

# Se definen las variables y su pasada por parametro
nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

#Salidas
print(f'Mi nombre es {nombre}')
print(f'Mi apellido es {apellido}')
print(f'Mi edad es {edad}')
print(f'El nombre del archivo es {sys.argv[0]}')
print(type(sys.argv))