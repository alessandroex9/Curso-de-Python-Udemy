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

produtos_10_de_porcentagem = [{'nome': p['nome'], 'preco': p['preco'] * 1.10} for p in produtos]
print(produtos_10_de_porcentagem)

produtos = produtos_10_de_porcentagem
print('_' * 130)

novosProdutos = [
    {'nome': 'Produto 6', 'preco': 15.00},
    {'nome': 'Produto 7', 'preco': 50.00},
]
novos_produtos = produtos_10_de_porcentagem + novosProdutos



produtos_ordenados_por_nome = sorted(novos_produtos, reverse=True, key=lambda item: item['nome'])
print(produtos_ordenados_por_nome)
print('_' * 130)

produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda item: item['preco'])
print(produtos_ordenados_por_preco)
print('_' * 130)