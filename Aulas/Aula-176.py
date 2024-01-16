"""
map - para mapear dados
"""

from functools import partial
def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},1
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_porcentagem = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)
"""
novos_produtos = [
    {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos
]
"""

def muda_preco_de_produto(produto):
    return {
        **produto,'preco': aumentar_dez_porcento(produto['preco'])
    }
novos_produtos = map(muda_preco_de_produto, produtos)

print_iter(produtos)
print_iter(novos_produtos)