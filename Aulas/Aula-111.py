"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembra-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

def soma1(*args):
    total = 0
    print(args, type(args))
    for numero in args:
        total = total + numero
        print(numero)        
        print(total)
    

soma1(1, 2, 3, 4, 5)
print(resto)