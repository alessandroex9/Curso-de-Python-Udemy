"""
faça um programa que peça para digitar um número inteiro,
Informe se este número é par ou ímpar. caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_do_usuario = input('Digite um número Inteiro: ')

try:
    numero_int = int(numero_do_usuario)
    if (numero_int % 2 == 0):
        print(f'O Número {numero_int} é Par!')
    else:
        print(f'O Número {numero_int} é Ímpar!')
except:
    print('O que vc digitou não é um número inteiro')