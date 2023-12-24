#Exercicio - Sistema de perguntas e respostas

perguntas =[
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','2','3','4','5'],
        'Respostas': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
print('Sistema de perguntas e respostas:')
for Pergunta in pergunta:   
    print('Pergunta:', pergunta[Pergunta])
    opcoes = perguntas['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print('-'*50)
    resposta = input('Digite a resposta:')
    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')