'''
Se tiene el archivo 'the-zen-of-python.txt' en el cuál aparecen algunas directrices
para el uso eficiente de python. Además se tiene el archivo words.py que contiene
una lista de palabras clave. Se pide:

a.- Leer ambos archivos y contar cuantas veces está presente cada palabra de words.py. 
Guardar el conteo en una nueva lista.

b.- Eliminar la(s) palabra(s) que tengan un conteo = 0 de la lista asignada al 
contenido de word.py

c.- Generar un diccionario que contenga las palabras restantes como 'key' y el 
conteo como 'value'. Imprimirlo como respuesta.
'''
with open("the-zen-of-python.txt") as f:
    zenofpython = f.read()

with open("words.py") as f1:
    words = f1.read()

words_count = []

words_count.append(zenofpython.split().count(words[0]))
words_count.append(zenofpython.split().count(words[1]))
words_count.append(zenofpython.split().count(words[2]))
words_count.append(zenofpython.split().count(words[3]))
words_count.append(zenofpython.split().count(words[4]))
words_count.append(zenofpython.split().count(words[5]))
words_count.append(zenofpython.split().count(words[6]))


print(words)

print(words_count, words)

# print(str(len(set(zenofpython))))
# print(str(len(set(words))))


