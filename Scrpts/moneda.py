import random

print("hola bienbenidos al juego cara o sello")

escoje = input("Ingresa tu eleccion; Cara o Sello: ").lower()

num = random.randint(1,2)

if num == 1:
    result = "cara"

elif num == 2:
    result = "sello"

if escoje == result:
    print("Bien echo, tu ganas")

else:
    print("Lo siento, tu pierdes cara o sello")

print("Gracias por jugar Cara o Sello")