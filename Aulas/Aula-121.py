"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iteráveis com as chaves 
values - iteráveis com os valores 
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga o útimo item adicionado
update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Alessandro',
    'sobrenome': 'Martins',
    'Idade': '18',
}

#Para retornar quantas chaves o dicionario tem
print(len(pessoa))
print('-'* 50)

#keys para retornar as chaves
print(pessoa.keys())
print('-'* 50)
print(list(pessoa.keys()))
print('-'* 50)
for chave in pessoa.keys():
    print(chave)
print('-'* 50)

#Values para retornar o valor
print(pessoa.values())
print('-'* 50)
print(list(pessoa.values()))
print('-'* 50)

for valor in pessoa.values():
    print(valor)
print('-'* 50)

#itens
print(pessoa.items())
print('-'* 50)
print(list(pessoa.items()))
print('-'* 50)

for itens, chave in pessoa.items():
    print(itens, chave)
print('-'* 50)

#setdefall cria um valor padrão caso não exista a chave
pessoa.setdefault('altura', None)
print(pessoa['altura'])
print('-'* 50)

