import math

def media(lista):
    return sum(lista)/len(lista)

def sdd(lista, media):
    diff = [(elemento - media) **2 for elemento in lista]
    return math.sqrt(sum(diff) / (len(lista) - 1))

def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor - m) / sd for valor in lista]
    return m, sd, lista_estandarizada

lista = [1, 2, 3, 4, 5, 6]

m, desv_st, l_e = resultado(lista)

print(f'La lista original es {lista}\nLa media es {m}\nLa desviacion estandart es {desv_st}\nLa lista estandarizada es {l_e}')