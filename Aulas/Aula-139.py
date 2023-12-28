lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)
print('-'* 50)

#List comprehension com mais de um for

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print('-'* 50)

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista)
