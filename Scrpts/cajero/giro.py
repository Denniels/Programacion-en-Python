def girar(saldo, cantidad):
    total = saldo - cantidad
    print(f'Su nuevo saldo es: ${total}')
    return total

if __name__ == '__main__':
    saldo = 10000
    cantidad = 1000
    girar(saldo, cantidad)

