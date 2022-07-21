
def validate(opciones, eleccion):# Definir validación de eleccion
    while opciones != list(opciones):
        if eleccion not in opciones:
                print(eleccion)
                
        else:
            print("Opción inválida, ingrese una opcion valida: ")

    #pass



if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    opciones = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)