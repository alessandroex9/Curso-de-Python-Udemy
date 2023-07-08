"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz', 'João']

lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)
print('-' * 25)
# Toda vez depois de usada enumerate zera
# Forma correta de se usar o enurate

for item in enumerate(lista):
    print(item)
print('-' * 25)

# Assim ele nunca zera a variavel

# Se você der um print na variavel enumerate
# ele ira imprimir o endereço da memoria
print(lista_enumerada)
print('-' * 25)

# Para ver o enumerate no print
# terá que converter ele antes para uma lista ou uma tupla

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
print('-' * 25)