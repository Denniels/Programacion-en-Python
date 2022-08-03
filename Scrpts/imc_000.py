import sys
peso = float(sys.argv[1])
altura = float(sys.argv[2])

imc = peso/(altura/100)**2

if imc < 18.5:
    clasif = 'Bajo de peso'
elif imc <25:
    clasif = 'Adecuado'
elif imc < 30:
    clasif = 'Sobrepeso'
elif imc < 35:
    clasif = 'Obesidad grado I'
elif imc < 40:
    clasif = 'Obesidad grado II'
else:
    clasif = 'Obesidad grado III'
# estructura condicional
print(f'Su IMC es {imc:.2f}')
print(f'La clasificación OMS es {clasif}')