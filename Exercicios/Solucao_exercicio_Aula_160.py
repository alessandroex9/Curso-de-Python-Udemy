"""
Exercicios
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profundo)
"""
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
"""
Ordene os produtos por nome decrescente (do maior para menor)----
Gere produtos_ordenados_por_nome por deep copy (Cópia profunda)----

Ordene os produtos por preco crescente (do menor paraa maior)---
Gere produtos_ordenados_por_preco por deep copy (Cópioa profunda)---
"""

import copy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)   
    ]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda p: p['nome'])

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')


print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')