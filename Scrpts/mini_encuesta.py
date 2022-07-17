preguntas = ['Enunciado pregunta 1', 'Enunciado pregunta 2', 'enunciado pregunta 3']

def imprimir_menu():
    print('Opciones')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

respuestas = []

for p in preguntas:
    print(p)
    imprimir_menu()
    respuestas.append(input('> '))

print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')

print(f'Gracias por responder la encuesta')


'''
todo esto se resume con funciones
# Inicio de preguntas

print(preguntas[0])
print('Opciones')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')
respuestas.append(input('> '))

print(preguntas[1])
print('Opciones')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')
respuestas.append(input('> '))

print(preguntas[2])
print('Opciones')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')
respuestas.append(input('> '))

print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')

print(f'Gracias por responder la encuesta')
'''