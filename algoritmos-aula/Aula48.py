"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a # Não copiara o valor mais sim o endereço
lista_c = []
print(lista_a)
print(lista_b)
print('-' * 25)

# O codigo abaixo vai adicionar um valor na lista_a,
# mais pois elas terem o mesmo endereço de mémoria
# o valor vai ser adicionado na lista_b tambem
lista_a.insert(0, 60)
print(lista_a)
print(lista_b)
print('-' * 25)

# Para copiar o valor de uma lista para a outra se usa o método copy()

lista_c = lista_a.copy()
print(lista_c)
print('-' * 25)