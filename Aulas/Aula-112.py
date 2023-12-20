"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembra-te de desempacotamento

def soma1(*args):
    total = 0
    for numero in args:
        total += numero
    return total           
    
    
soma_1_2_3 = soma1(1,2, 3)

print(soma_1_2_3)

soma_4_5_6 = soma1(4, 5, 6)

print(soma_4_5_6)

outra_soma = soma1(424,5333,676)
print(outra_soma)

print(sum((424,5333,676)))#Uma função para soma ela já é propria do Python

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9

outra_soma1 = soma1(*numeros)# Eu tenho que passar assim para dar certo

print(outra_soma1)