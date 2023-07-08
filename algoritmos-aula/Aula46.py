"""
Lista em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conchecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
append - Adiciona um item ao final
insert - Adiciona um item no índece escolhido
pop
del
clear
extend 
+
Create Read Uptade  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [8, 17, 4, 22, 9, 15, 12, 6, 19, 2]

# Adicionando itens em qualquer índice da lista com o insert
print(lista)
#lista.insert(O primeiro argumento eo índice, 
# O segundo argumento eo valor que vai ser adicionado)
lista.insert(0, 24274)
print(lista)
lista.insert(3, 'Ale')
print(lista)
print('-' * 25)

# O comando clear serve para limpa toda a lista
numeros = [5, 9, 2]
print(numeros)
numeros.clear()
print(numeros)
print('-' * 25)