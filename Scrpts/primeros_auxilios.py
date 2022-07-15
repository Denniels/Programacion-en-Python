
estimulo = input('Responde a estimulos ').lower()
if estimulo == str("si"):
    print('Llevarlo al hospital mas cercano')

else:
    print('Abrir via aerea')
    respira = input('Respira ').lower()
    if respira == str('si'):
        print('Permitir posicion de suficiente respiracion')
    else:

        
        print('Administrar 5 ventilaciones y llamar a una ambulancia ')
        vida = input('¿Signos de vida? ').lower()
        if vida == str('si'):
            print('Reevaluar la espera de la ambulancia')
            ambulancia = input('Llego la ambulancia ')

        


        else:
            print('Administrar compreciones toracicas hasta que llegue la ambulancia')
            


    