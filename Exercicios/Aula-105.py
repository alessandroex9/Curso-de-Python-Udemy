"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas e receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por patrão, funções Python retornam None (nada).
"""
def minhafuncao1():
    print('Várias')
    print('Várias')

def minhafuncao2(a, b):
    print(a, b)
    
minhafuncao1()
minhafuncao2(1, 2)
minhafuncao2(3, 4)

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Alessandro')
saudacao('Maria')
saudacao('José')

def saudacao2(nome='sem nome'):
    print(f'Olá, {nome}!')

saudacao2('Alessandro Martins')
saudacao2()