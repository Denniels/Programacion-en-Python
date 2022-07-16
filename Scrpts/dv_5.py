d = sum([int(n)*(i%6+2)for i,n in enumerate(input('Ingresa tu rut sin digito verificador: 12345678 ')[::-1])])%11
print('Su digito verificador es: ','K'if(d==1)else 11-d)