"""
Exercicios
Iterando strings com while
"""
nome = 'Alessandro'

indice = 0
nova_str = ''

while indice < len(nome):
    letra = nome[indice]
    
    nova_str += f'*{letra}'

    indice += 1
nova_str += '*'
print (nova_str)