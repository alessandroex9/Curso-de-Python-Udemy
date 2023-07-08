"""
Lista em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conchecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#       +01234
#       -54321
srtring = 'ABCDE' # 5 caracteres (len)
# Formas de criar uma lista
lista1 = list('João', 'Maria', 5)
lista2 = ['João', 'Maria', 5]
print(lista1)
print(lista2)

#Como acessar cada índice
print(lista2[1], type(lista2[1]))

#Como alterar os valores das listas

lista2[1] = 'Maria Pereira'
print(lista2[1], type(lista2[1]))