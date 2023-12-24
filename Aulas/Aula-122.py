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
import copy #Vai ser usada na linha 34

d1 = {
    'c1': '1',
    'c2': '2',
    'c3': '3',
    'l1': [0, 1, 2],
}

#Copy faz uma cópia rasa do dicionario
d2 = d1.copy()
print(d2)
print('-'* 50)
d2['c1'] = 1000 #aqui o d1 não vai ser alterado
d2['l1'][1] = 999 #aqui o d1 vai ser alterado por se tratar de uma lista dentro do dicionario
print(d1)
print(d2)
print('-'* 50)

# Para fazer uma copia total tem que import copy
# Para se usar o Deep copy  (copia profunda)
d2 = copy.deepcopy(d1)

print(d2)
print('-'* 50)
d2['c2'] = 77  
d2['l1'][2] = 10000 #Agora a copia foi total conseguindo alterar tudo não dicionario
print(d1)
print(d2)