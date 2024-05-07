"""
Tipo tupla - Uma lista imutável
tupla uma lista que não pode ser mudada
Assim como as variaveis
"""
# Exemplo de lista
nomes = ['Maria', 'Helena', 'Luiz']

# Como criar uma lista
# Só não colocar entre [] os valores
nomes1 = 'Maria', 'Helena', 'Luiz'
print(nomes1)
# uma tupla pode ser craida com os valores entre ()
# nomes1 = ('Maria', 'Helena', 'Luiz')
print('-' * 25)

# Como converter uma lista para uma tupla
nomes = tuple(nomes)
print(nomes)