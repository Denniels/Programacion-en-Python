def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def productoria(prod_1) :    
    result = 1
    for x in prod_1:
         result = result * x 
    return result

def calcular(**parametros):
    for key, value in parametros.items():
        if type(value) == int:
            print(f"El factorial de {value} es {factorial(value)}")

        elif type(value) == list:
            print(f"La productoria de {value} es {productoria(value)}")        

calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)