from string import ascii_lowercase

comparacion = ascii_lowercase

contrasena = input('Ingrese una contraseña: ').lower()

n_intentos = 0

for comp1 in contrasena:
    for comp2 in comparacion:
        n_intentos += 1
        if comp1 == comp2:
            break

print(f'La contraseña fue forzada en {n_intentos}')