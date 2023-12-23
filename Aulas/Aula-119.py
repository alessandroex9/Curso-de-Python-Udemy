"""
Dicionário em Python (tipo dict)
Dicionário são 3estruturas de dodas do tipo
par de 'chave' e 'Valor'
Chaves podem der consideradas como o 'índice'
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc...
O valor pode ser de qulaquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionário.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'luiz Otávio',
    'sobrenome': 'Miranda',
    'Idade': '18',
    'altura': '1.8',
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}   
    ]
}
"""
pessoa = {
    'nome': 'Alessandro',
    'sobrenome': 'Martins',
    'Idade': '18',
    'altura': '1.8',
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},  
    ],
}
#pessoa = dict(nome= 'Alessandro', sobrenome='Martins')
print(pessoa, type(pessoa))
print('-' * 50)
    
print(pessoa['endereços'])
print('-' * 50)

for chave in pessoa:
    print(chave, pessoa[chave])