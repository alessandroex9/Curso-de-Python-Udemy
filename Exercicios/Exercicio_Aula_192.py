"""
Exercício - Lista de Tarefas com desfazer e refazer
Músicas para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] ->
todo = ['fazer café'] -> Adiciona fazer café
todo = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Reazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""
tarefas = []
tarefas_geral = []
tarefas_removida = []

def adicionar_tarefa(entrada):
    tarefas.append(entrada)
    tarefas_geral.append(entrada)
    return tarefas

def listar():
    print('Tarefas: ', tarefas)

def desfazer():
    if not tarefas:
        print('Nada par desfazer')
    else:
        tarefa_removida = tarefas.pop()
        tarefas_geral.remove(tarefa_removida)

def refazer():
    if not tarefas_geral:
        print('Nada para resfazer')

    else:
        tarefa_refeita = tarefas_geral.pop()
        tarefas.append(tarefa_refeita)


while True:
    print('Comandos: listar, desfazer, refazer')
    entrada = input('Digite uma tarefa ou comando: ')

    if entrada == 'listar':
        listar()

    elif entrada == 'refazer':
        refazer()
        print('Tarefas: ', tarefas)

    elif entrada == 'desfazer':
        desfazer()
        print('Tarefas: ', tarefas)

    else:
        adicionar_tarefa(entrada)
