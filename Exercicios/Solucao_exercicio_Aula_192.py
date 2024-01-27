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
tarefa = []
tarefas_refazer = []

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


while True:
    print('Comandos: listar')
    tarefa = input('Digite uma tarefa ou comando: listar, desazer e refazer')

    if tarefa == 'listar':


    elif tarefa == 'desfazer':

    elif tarefa == 'refazer':

    else:

