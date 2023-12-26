"""
Função lambda em Python
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. ou seja, tudo
deve ser contido dentro de uma única
expressão.
"""
lista = [
    {'nome':'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Edurdo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista1 = [4, 5, 12, 77, 81, 1, 0]
#para ordenar a lista
lista1.sort()
#sorted(lista)
print(lista1)
print('-'*50)
lista1.sort(reverse=True)
print(lista1)
print('-'*50)

# O Python usa a tabela Unicode para ordenar
"""
def ordena(item):
    print(item)
    return item ['nome']
"""
print('-'*50)

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)
    print('-'*50)

def exibir(lista):
    for item in lista:
        print(item)
    print('-'*50)

l1= sorted(lista, key=lambda item: item['nome'])
l2= sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
