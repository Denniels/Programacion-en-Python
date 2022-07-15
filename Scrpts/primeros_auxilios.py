estimulos = input("¿Responde a estimulos?: ").lower()

if estimulos == 'si':
    print ('Valorar la necesidad de llevarlo al hospital mas cercano')

else:
    print ('Abrir la via Aérea')
    respira = input("¿Respira?: ").lower()

    if respira == 'si':
        print ('Permitirle posición de suficiente ventilación')

    else:
        print ('Administrar 5 Ventilaciones y llamar a Ambulancia')
        ambulancia = 'no'

        while ambulancia == 'no':
            signos = input("¿Signos de Vida?: ").lower()

            if signos == 'si':
                print ('Reevaluar a la espera de la Ambulancia')           
                ambulancia = input("¿Llegó la Ambulancia?: ").lower()

            else:
                print ('Administrar Compresiones Torácicas hasta que llegue ambulancia')
                ambulancia = input("¿Llegó la Ambulancia?: ").lower()

print ('Fin')


    