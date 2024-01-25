"""
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
"""
import json
import os
"""
pessoa = {
    'nome': 'Alessandro Martins',
    'sobrenome': 'Santos',
    'enderecos':[
        {'rua': 'A', 'numero': 32},
        {'rua': 'B', 'numero': 55}, 
    ],
    'altura': 1.8,
    'numero_preferidos': (5, 7, 10, 77, 96, 97),
    'dev': True,
    'nada': None,
}

with open('aula-190.json', 'r', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)
"""

with open('aula-190.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa)

