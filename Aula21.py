"""
Fatiamento de strings 
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i - Inicio, f - Fim, p - Passo
Obs.: a função len() retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'

print(variavel[4:8])
print(10 *'_')
print(variavel[4:])
print(10 *'_')
print(variavel[:8])

print(10 *'_')
print(len(variavel))
print(10 *'_')
print(variavel[0:len(variavel):2])
print(10 *'_')
print(variavel[::-1])