valor = int(input("Ingrese un valor a probar "))

if valor < 0:
    print(''' Cuidado, los criterios de paridad normalmente
se utilizan con mumeros positivos.
 Usar el resultados con precaucion.''')

elif valor == 0:
    print(f"Este valor,{valor}, es cero")

elif valor % 2 == 0:
    print(f"Este numero, {valor}, es par")

else:
    print(f"Este numero, {valor}, es impar")