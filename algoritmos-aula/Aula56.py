"""
split e join com list e str
slipt - divide uma string
join - une uma string
"""
frase = "Olha só que, coisa interessante"
print(frase)

# Split para dividir a frase em uma lista com as palavras
# Se chamar o metodo split e não passar nem um argumento
# ela será dividida nos espaços em branco

lista_palavras = frase.split()
print(lista_palavras)
print(len(lista_palavras))
print('-' * 25)

# Se voce quiser dividir ne uma caractere especifica
# mais quando voce usa isso o caratere some(Não vai fazer parte da lista)

lista_palavras_dividida = frase.split(',')
print(lista_palavras_dividida)
print(len(lista_palavras_dividida))
print('-' * 25)

# Existe um metodo Strip() que some com os espaços do começo e do fim.

lista_palavras_strip = frase.strip()

print(lista_palavras_strip)
print(len(lista_palavras_strip))
print('-' * 25)

# Usando o strip com um for
for i, frase in enumerate(lista_palavras_strip):
    print(lista_palavras_strip[i].strip())
print('-' * 25)

# Existe o rstrip que só corta os espaço da direita
# E o lstrip que só corta os espaços da esquerda

# metodo join
lista_2 = 'O céu é bonito'
frase_unida = '-'.join(lista_2)
print(frase_unida)
print('-' * 25)

lista_palavras_strip_join = '_'.join(lista_palavras_strip)
print(lista_palavras_strip_join)
print('-' * 25)
# O join só funciona com listas, tuplas e Str