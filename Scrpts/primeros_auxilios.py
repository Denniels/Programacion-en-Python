ambulancia=('no')
estimulos = input("¿Responde a Estimulos? [Si/No]: ").lower()

# if (estimulos!='si' or estimulos!='no'):
#     print('Debe ingresar solo Si o No..')

if (estimulos=='si'):
    print ('Valorar la necesidad de llevarlo al hospital mas cercano')
    #print ('Fin')
else:
    print ('Abrir la via Aérea')
    respira = input("¿Respira? [Si/No]: ").lower()
    # if (respira!='si' or respira!='no'):
    #     print('Debe ingresar solo Si o No..')
    if (respira=='si'):
        print ('Permitirle posición de suficiente ventilación')
        #print ('Fin')
    else:
        print ('Administrar 5 Ventilaciones y llamar a Ambulancia')
    
        while (ambulancia=='no'):
            signos = input("¿Signos de Vida? [Si/No]: ").lower()
            if (signos=='si'):
                print ('Reevaluar a la espera de la Ambulancia')           
                ambulancia = input("¿Llegó la Ambulancia? [Si/No]: ").lower()
            else:
                print ('Administrar Compresiones Torácicas hasta que llegue ambulancia')
                ambulancia = input("¿Llegó la Ambulancia? [Si/No]: ").lower()
print ('Fin')


    