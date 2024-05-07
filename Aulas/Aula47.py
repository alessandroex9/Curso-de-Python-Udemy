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
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]

#Contatenando e estendendo listas em Python
lista_3 = lista_1 + lista_2
print(lista_1)
print('-' * 25)
print(lista_2)
print('-' * 25)
print(lista_3)
print('-' * 25)

# Fazendo a contatenação com o método extend
print(lista_1)
# O extend abaixo vai aplicar a lista_3 na lista_1
# Como se um tivese fazendo essa junção lista_1 = lista_1 + lista_3
lista_1.extend(lista_3)
print(lista_1)
print('-' * 25)