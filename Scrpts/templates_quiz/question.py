import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    p.pool_preguntas
    preguntas =  p.pool_preguntas[dificultad].keys()

    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido =  random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas

    if n_elegido == 1:
        numpregun ="pregunta_1"
    elif n_elegido == 2:
        numpregun ="pregunta_2"
    else:
        numpregun ="pregunta_3"      
    
    #print(p.pool_preguntas[dificultad][numpregun])
    pregunta = p.pool_preguntas[dificultad][numpregun]["enunciado"]

    alternativas = shuffle_alt(p.pool_preguntas[dificultad][numpregun])
    
    return pregunta[0],alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')