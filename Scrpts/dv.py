rut = input("Ingresa tu rut sin digito verificador: 12345678: ")
rut_list = []
serie = [2, 3, 4, 5, 6, 7, 2, 3]

for i in rut:
    rut_list.append(i)

inver_rut = [num for num in reversed(rut_list)]

for j in range(len(inver_rut)):
    inver_rut[j] = int(inver_rut[j])

multi_list = [x * y for x,y in zip(inver_rut,serie)]

suma = sum(multi_list)

modulo = suma % 11

resto = 11 - modulo

if resto == 10:
    print('Su digito verificador es K')
    
elif resto == 11:
    print('Su dijito verificador es 0')

else:
    print(f'Su digito verificador es {resto}')