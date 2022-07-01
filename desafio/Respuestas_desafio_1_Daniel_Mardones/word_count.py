import sys # librería que contiene la función sys.argv, para ingresar parámetros por consola.
'''
Guardamos el argumento en una variable
y le indicamos el tipo de dato
'''
file = str(sys.argv[1])

with open(file, "r") as file: # realizamos la lectura del archivo
    texto = file.read()
    file.close() #El whith open cierra el archivo, pero por seguridad es buena práctica cerrarlo

palabras = texto.split(" ") # Variable para separar por espacio las palabras del string

palabras_tmp = [] # Lista vacía para agregar los datos de la siguiente función for

'''
Esta es una función, que nos permite iterar palabra por palabra dentro de la lista palabras
y agregar a la lista palabras_tmp si la palabra no se encuentra en esta lista, con esto, 
guardamos solo las palabras que se repiten, esta función se repite para los caracteres
'''

for palabra in palabras:
    if palabra not in palabras_tmp:
        palabras_tmp.append(palabra)

#print(len(palabras_tmp))
# variable para almacenar las palabras repetidas y con la función len contamos los elementos de la lista
contador_palabras = len(palabras_tmp)

caracter_tmp = []

for caracter in texto:
    if caracter not in caracter_tmp:
        caracter_tmp.append(caracter)

#print(len(caracter_tmp))

contador_caracter = len(caracter_tmp)

# Salida
print(f"El número de caracteres distintos es: {contador_caracter}\nEl número de palabras distintas es: {contador_palabras}")
# opción usando .format, pero es mas elegante hacerlo usando f
#print("El numero de numero de caracteres distintos es: {}\nEl numero de palabras distintas es: {}".format(contador_caracter, contador_palabras))

'''
Esta es la forma sencilla de hacerlo, pero me gusta python y espero poder aprender
mucho más con estas prácticas, de todas maneras ambas formas son válidas de resolver el problema
'''
#print(str(len(set(texto))))
#print(str(len(set(palabras))))