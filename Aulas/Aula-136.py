"""
List comprehension em Python
list comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""

print(list(range(10)))
print('-'* 50)

lista = []

for numero in range(10):
    lista.append(numero)

print(lista)
print('-'* 50)

#List comprehension
lista1 = [numero for numero in range(10)]
print(lista1)
print('-'* 50)

lista2 = [numero * 2 for numero in range(10)]
print(lista2)
print('-'* 50)