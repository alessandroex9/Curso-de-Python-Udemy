"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

variavel1 = soma(1, 2)
print(variavel1)

variavel2 = int(1)
print(variavel2) #Vai me retornar o valor inteiro

variavel3 = print('Alessandro')

print(variavel3) #Vai aparecer none na tela e não o Alessandro

print('-' * 25)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)

print('-' * 25)
print(soma(11, 55))#Vai entrar na condição