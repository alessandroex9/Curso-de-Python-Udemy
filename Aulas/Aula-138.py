"""
List comprehension em Python
list comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""
import pprint

def p_print(valor):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    produto for produto in produtos
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
"""
print(novos_produtos)
print('-'* 50)
print(*novos_produtos, sep='\n')
print('-'* 50)
"""

p_print(novos_produtos)
print('-'* 50)
"""
Filtro é diferente de map.
Filtro eu não quero incluir determinada coisa na minha lista
se a coindição que eu passar for verdadeira
"""
lista = [n for n in range(10) if n < 5]

print(lista)
print('-'* 50)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # A condição do mapeamento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    # A condição do filtro
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

p_print(novos_produtos)