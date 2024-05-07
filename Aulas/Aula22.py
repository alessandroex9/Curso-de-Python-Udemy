"""
Exercicio
Peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome Invertido é {nome Invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite Sua idade: ')

if nome and idade:
    print(f'Seu Nome é {nome}')
    print(f'{nome} Invertido é: ', nome[::-1])
    if ' ' in nome:
        print('Seu nome Contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'{nome} contém ', len(nome), 'Letras')
    print(f'A primeira letra de {nome} é: ', nome[0])
    print(f'A última letra de {nome} é: ', nome[-1])
else:
    print('Desculpe, você deixou campos vazios.')