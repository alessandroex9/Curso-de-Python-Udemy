"""
Exercício com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorna o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
def par_ou_impar(x):
    if x % 2 == 0:
        return 'Par'
   
    return 'Ímpar'
    
multiplicacao = multiplicar(1, 2, 3, 4, 5)
print("O resultado da multiplicação é: ", multiplicacao)

resultado = par_ou_impar(5)
print('O numero passado é: ', resultado)