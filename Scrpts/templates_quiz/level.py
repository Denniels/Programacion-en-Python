def choose_level(n_pregunta, p_level):
    '''
    n_pregunta --> turno pregunta, asignación de nro
    p_level --> nro preguntas por nivel

    p_level = 1

    1.- basica         p == nro
    2.- media          2*P == nro
    3.- avanzada       3*p == nro


    1 basica          1*p_level basic
    2 intemedia       2*p_level interm
    3 avanzada        3*p_level avanzado
    p_level = 2

    1.- basica         p > nro
    2.- basica         p == nro
    3.- media          2p > nro
    4.- media          2p == nro
    5.-avanzada        2p < nro
    6.- avnzada        3p == nro 

    1 y 2 basicas     1*p_level >= n_pregunta  basico
    3 y 4 intermedia  2*p_level >= n_pregunta intermedo
    5 y 6 avanzadas   2*P_level < n_pregunta

    p_level = 3

    1. basica          p >
    2.- basica         P >
    3.- basica         p ==
    4.- media          2p >
    ....               2p >
                       2p ==

    1,2,3 basica
    4,5,6 intermedia
    7,8,9 avanzad
    '''
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
      level = 'basicas'
    elif n_pregunta <= 2*p_level:
      level = 'intermedias'
    else: level = 'avanzadas'
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
