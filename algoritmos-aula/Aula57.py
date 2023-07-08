"""
Listas de listas e seus índices
"""
salas = [
    #0           1
    ['Maria', 'Helena', ], # 0 
    #0
    ['Elaine', ], # 1
    #0           1        2          3
    ['Luiz', 'João', 'Eduarda',(0, 8, 7, 9) ], # 2
]

print(salas)
print(type(salas))
print('-' * 25)
print(salas[1])
print('-' * 25)
print(salas[0][1])
print('-' * 25)
print(salas[2][2])
print('-' * 25)
print(salas[2][3][2])
print('-' * 25)
print(salas[2][3][3])

for sala in salas:
    print(sala)
    print('-' * 25)
    alunos = [sala]
    for alunos in sala:
        print(alunos)
print('-' * 25)