# Operadores in e not in
# Strings são iteráveis
#   0 1 2 3 4 5 6 7 8 9 
#   A l e s s a n d r o
# -10-9-8-7-6-5-4-3-2-1
nome = 'Alessandro'

print(nome[5])
print(nome[-5])

print('ssa' in nome)
print('ddd' in nome) 
print('ddd' not in nome)
print('ssa' not in nome) 



nome = input('Digite seu nome: ')
encontar = input('Digite o que voce quer encontar: ')

if encontar in nome:
    print(f'{encontar} está em {nome}')

else:
    print(f'{encontar} não está em {nome}')