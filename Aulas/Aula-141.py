"""
Dictionary Comprehension e Set Comprehension
"""
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
for chave, valor in produto.items():
    print(chave, valor)
print('-' * 50)
dc = {
    chave: valor
    for chave, valor in produto.items()    
}

print(dc)
print('-' * 50)

dc1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'    
}
print(dc1)
print('-' * 50)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc2 = {
    chave: valor
    for chave, valor in lista
}

print(dc2)
print('-' * 50)

s1 = {i ** 2 for i in range(10)}
print(s1)