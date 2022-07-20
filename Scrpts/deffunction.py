def elevar(x):
    print(x**2)

def eleva_2(x,y,z):
    print('Este es el valor de x al cuadrado',x**2)
    print('Este es el valor de y al cuadrado',y**2)
    print('Este es el valor de z al cuadrado',z**2)

elevar(4)
elevar(5)
elevar(8)

i=9

eleva_2(16, 22, i)

def prueba_return():
    a = 'Esta linea se va a imprimir'
    b = 'Esta linea no se va imprimir'
    return a
    print(b) # Este print no aparece

print(prueba_return())

def elevar_3(base, expoponente):
    x = base**expoponente
    return x

print(elevar_3(2,2))
print(type(elevar_3(2,2)))

def extremos(lista):
    minimo = min(lista)
    maximo = max(lista)
    print(f'El valor minimo es {minimo}')
    print(f'El valor maximo es {maximo}')
    return minimo, maximo

i, f = extremos([2, 34, 5, 3, 23, 2])

def calculo_extremos(x, y):
    t = (x+y)/y
    return t

valor_t = calculo_extremos(i, f)
print(valor_t, type(valor_t))

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

def filtrar(i,j):
    filtro = {k:v for k,v in i.items() if v > j}
    return filtro
    print(filtro)

print(filtrar(precios, 100000))

def calculo(x,y,z):
    r = (x+y)/y+z
    return r

varieble_1 = calculo(12,1,20)
print(varieble_1)