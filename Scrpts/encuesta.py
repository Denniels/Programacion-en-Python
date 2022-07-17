preguntas = ['Enunciado pregunta 1', 
             'Enunciado pregunta 2', 
             'Enunciado pregunta 3',
             'Enunciado pregunta 4',
             'Enunciado pregunta 5',
             'Enunciado pregunta 6',
             'Enunciado pregunta 7',
             'Enunciado pregunta 8',
             'Enunciado pregunta 9',
             'Enunciado pregunta 10']

def imprimir_menu_3():
    print('Opciones')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

def imprimir_menu_4():
    print('Opciones')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')
    print('4) Prefiero no responder')

respuestas = []

for i, p in enumerate(preguntas):
    print(p)
    if i in [2,5,8]:
        imprimir_menu_4()
    else:
        imprimir_menu_3()
    respuestas.append(input('> '))
# Mostrar respuestas
for k in range(9):
    print(f'La respuesta a la pregunta {k+1} fue {respuestas[k]}')


print(f'Muchas gracias por responder la encuesta')