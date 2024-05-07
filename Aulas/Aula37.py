"""
while/else
"""
string = 'Alessandro'

i = 0
while i < len(string):
    letra = string[i]

    if letra == "a":
        print('Fim')
        break

    print(letra)
    i += 1

else:
    print('Não encontrei um a')

print('Fora do While')

