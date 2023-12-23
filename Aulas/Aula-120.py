"""
Manipulando chaves e valores em dicionários
"""
pessoa = {
    'sobrenome': 'Martins',
    'Idade': '18',
    'altura': '1.8',
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},  
    ],
}
"""
primeiro modo
pessoa['nome'] = 'Luiz Otávio'
lista  = []
"""
# Segundo modo dinamico
pessoa['nome'] = 'Alessandro'
lista = []

chave = 'nome'
pessoa[chave] = 'luiz Otávio'
lista = []

print(pessoa)
print(pessoa['nome'])

print('-'*50)
#Criando um novo item
pessoa['telefone'] = '123456'

print(pessoa)
print(pessoa['telefone'])

print('-'*50)
#Apagando um item
del pessoa['telefone']
print(pessoa)

print('-'*50)
# Para saber se um item existe
if pessoa.get('telefone') is None:
    print(' Não Existe')

else:
    print(pessoa['telefone'])
    print('Existe')