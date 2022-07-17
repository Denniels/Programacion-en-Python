from giro import girar

def check(saldo, cantidad, funcion):
    if saldo < cantidad:
        print(f'No se puede aplicar la operación solicitada. Su saldo es ${saldo}')
        error = True
    else:
        saldo = funcion(saldo, cantidad)
        error = False
        return saldo, error

if __name__ == '__main__':
    saldo = 10000
    cantidad1 = 11000
    saldo, error = check(saldo, cantidad1, girar)
    cantidad2 = 9000
    saldo, error = check(saldo, cantidad2, girar)
