prod_1 =  [4, 6, 7, 4, 3] 
fact_1 = 5
fatc_2 = 6 

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def productoria(prod_1) :    
    result = 1
    for x in prod_1:
         result = result * x 
    return result

print("El factorial de",fact_1,"es", factorial(fact_1))
print("La productoria de",prod_1,"es", productoria(prod_1))
print("El factorial de",fatc_2,"es", factorial(fatc_2))


