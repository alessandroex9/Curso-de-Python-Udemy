"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculina', 'feminina', 'unisex'],
    ['algodão', 'poliester'],
]

print(list(combinations(pessoas, 2)), sep='\n')

print('-' * 100)
def print_iter(iterador):
    print(*list(iterador), sep='\n')


print_iter(combinations(pessoas, 3))
print('-' * 100)
print_iter(permutations(pessoas, 2))


print_iter(product(*camisas))