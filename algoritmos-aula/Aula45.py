"""
Lista em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conchecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
append, insert, pop, del, clear, extend, +
Create Read Uptade  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
print('-' * 25)

# Passando um Valor de uma lista e passando para uma váriavel
numero = lista[2]
print(numero)
print('-' * 25)

# Mudando um valor de índice da lista (Uptade)
lista[2] = 1000
print(lista)
print('-' * 25)

# Apagando um valor da lista (Delete)
print(lista)
print(lista[2])
del lista[2]
print(lista)
print(lista[2])
print('-' * 25)

# Adicionando um elemento a lista (Insert)
print(lista)
lista.append(98765)
lista.append(-902)
lista.append(123.764)
print(lista)
print('-' * 25)

# Como remover o último elemento da lista 

print(lista)
lista.pop() # pop() sem valor remove o último elemento da lista
print(lista)
print('-' * 25)

print(lista)
lista.pop(5) # o pop com índice remove o valor do índice passado
print(lista)
print('-' * 25)