"""
Desempacotamento em chamadas
de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# Desenpcotando uma lista
primeiro, b, c, *resto, ultimo= lista
print(primeiro, c, b, ultimo)

# Exemplo de desenpactamento em chamadas de funções
for nome in lista:
    print(nome, end=' ')
    
print('-' * 25)
# A mesma coisa que o forma mais de forma mais prática
print(*lista) # Mesma que # print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print('-' * 25)

print(*string, sep='\n')
print('-' * 25)

print(*tupla, sep='\n')
print('-' * 25)