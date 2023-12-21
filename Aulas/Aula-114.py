"""
Higher Order Functions
Funções de primeira classe
"""
"""
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

print(saudacao('Bom dia!', 'Alessandro'))
print('-' * 25)

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Boa Tarde!', 'Alessandro')

print(v)