frase = 'O Python é uma linguagem de programação de '\
    'Multiparadigma. '\
    'O Python foiu criado por Guido van Rossum.'
i = 0
qtd_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
        

    if qtd_mais_vezes < qtd_atual:
        qtd_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual
    
    print(letra_atual, qtd_atual)

    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_que_apareceu_mais_vezes}" que aperceu '
      f'{qtd_mais_vezes} x')