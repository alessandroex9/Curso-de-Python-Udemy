"""
Introdução ao desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']

# Desempacota
nome1, nome2, nome3 = nomes
print(nome2)
print('-' * 25)

# Como pegar um itens especifico da lista
nome1, *resto = nomes
print(nome1)
print(resto)
print('-' * 25)

# Como pegar um itens do meio da lista
_ = 0 # OBS. Quando se cria um variavel que não será mais usada se 
# coloca o nome de  '_' para que se outro desenvolvedor for 
# ler o meu código ele saiba que essa variavel não será mais usada
_, nome2, *_ = nomes
print(nome2)
print(_)