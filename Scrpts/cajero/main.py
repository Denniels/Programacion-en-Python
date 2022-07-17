import sys
from deposito import depositar
from giro import girar
from chequeo import check

menu_principal = '''¡Bienvenido al Banco Amigo!. Escoja una opción:
                    1. Consultar saldo
                    2. Hacer depósito
                    3. Realizar giro
                    4. Salir
                    > '''

def mostrar_menu(saldo = 0):
    opcion =''

    while opcion != 4:
        opcion = int(input(menu_principal))

        if opcion > 0 and opcion < 5:
            if opcion == 1:
                print(f"Su saldo es de: {saldo}")

            elif opcion == 2:
                cantidad = int(input("Ingrese cantidad: "))
                saldo = depositar(saldo, cantidad)

            elif opcion == 3:
                if saldo > 0:
                    error = True
                    while error:
                        cantidad = int(input("Ingrese cantidad: "))
                        saldo, error = check(saldo, cantidad, girar)

                else:
                    print("No puede realizar giros. Su saldo es de 0.")

            elif opcion == 4:
                print("Saliendo")
                
        else:
            print("Opción inválida. Ingrese 1, 2, 3 ó 4.")

if len(sys.argv) == 2:
    mostrar_menu(int(sys.argv[1]))
else:
    mostrar_menu()


