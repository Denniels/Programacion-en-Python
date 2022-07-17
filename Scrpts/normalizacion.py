import math

def modulo(lista):
    return math.sqrt(sum([elemento**2 for elemento in lista]))
    
def normalizar(lista):
    mod = modulo(lista)
    return [elemento/mod for elemento in lista]

vector = [1, 2, 3, 4, 5, 6]
print(normalizar(vector))
