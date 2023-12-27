"""
List comprehension em Python
list comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""

#Mapeamento de dados em List comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    produto for produto in produtos
]

print(novos_produtos)
print('-'* 50)
print(*novos_produtos, sep = '\n')
print('-'* 50)

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]

print(novos_produtos)
print('-'* 50)
print(*novos_produtos, sep = '\n')
print('-'* 50)

# Usando o mapeamento para fazer um calculo de porcentagem sobre o preço
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
print(novos_produtos)
print('-'* 50)
print(*novos_produtos, sep='\n')
print('-'* 50)

# Usando o mapeamento para fazer um calculo de parcentagem sobre o preço usando condicional
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos)
print('-'* 50)
print(*novos_produtos, sep='\n')
print('-'* 50)