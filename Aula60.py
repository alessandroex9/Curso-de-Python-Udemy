"""
Operação ternária (Condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro Valor')
print('-' * 25)

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)
print('-' * 25)

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)
print('-' * 25)

# Exemplo
digito = 4 # Se fosse por exemplo 90 ele seria 0.

novo_digito = digito if digito <= 9 else 0

print(novo_digito)
print('-' * 25)

# Exemplo 2

digito_2 = 67 # Se ele fosse menor entre 0 e 9 ele seria ele mesmo.

novo_digito_2 = 0 if digito_2 > 9 else digito_2

print(novo_digito_2)
print('-' * 25)