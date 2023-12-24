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
#Get para obter o nome da chave
print(pessoa.get('nome'))
print('-'* 50)

#Pop Ele vai me retornar o valor e depois apagar a chave
nome = pessoa.pop('nome')
print(pessoa)
print('-'* 50)

# popitem elimina a ultima chave do dicionario
Idade = pessoa.popitem()
print(Idade)
print('-'* 50)
print(pessoa)
print('-'* 50)


#Update ele atualiza o dicionario
pessoa.update({
    'sobrenome':'Santos',
    'Altura':'1.8',# Tambem pode criar uma nova chave
})
print(pessoa)
print('-'* 50)
#tambem pode ser usada assim
pessoa.update(sobrenome='Martins dos Santos', Altura='1.79')
print(pessoa)
print('-'* 50)
#tambem pode ser usada com tupla ou listas
tupla = ('nome', 'Alessandro'),
pessoa.update(tupla)
print(pessoa)
print('-'* 50)

lista = [['nome','Ale'], ['idade',24]]
pessoa.update(lista)
print(pessoa)