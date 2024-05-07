"""
Faça um programa que peça o primeiro nome do usúario. Se o nome tiver 4 letras 
ou menos escreva "Se nome é curto"; se tiver entre 5 e 6 letras,
escreva "Sue nome é normal":
maior que 6 escreva "Seu nome é muito grande"
"""
nome = input('Digite sue nome: ')

comprimento = len(nome)

if comprimento > 1:
    if comprimento <= 4:
        print(f'O nome {nome} tem {comprimento} Letras')
        print('Então ele é curto!')
    elif comprimento >= 5 and comprimento <= 6:
        print(f'O nome {nome} tem {comprimento} Letras')
        print('Então ele é Normal!')
    else:
        print(f'O nome {nome} tem {comprimento} Letras')
        print('Então ele é Muito Grande!')
else:
    print('Digite algo válido!')