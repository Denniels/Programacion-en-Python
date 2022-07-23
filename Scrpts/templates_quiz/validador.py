def validate(numeros, eleccion):# Definir validación de eleccion
    while True:
        if eleccion not in numeros:
            print('Opcion invalida, ingrasa un opcion valida')

        else:
            return eleccion

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    opciones = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)