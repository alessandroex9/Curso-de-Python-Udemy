"""
Criando arquivos com Python
Usamos a função open para abrir
um arquivo em python (ele pode ou não existir)
Modos:
r (leitura), w(escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
context maneger - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linhas)
readlines (ler linhas)
Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
"""

caminho_arquivo = 'C:\\Users\\aless\\OneDrive\\Documentos\\MeusProjetos\\Secao-4-do-curso-de-python\\aula186.txt'

#Com o with o qruivo vai ser aberto e fechado automaticamente
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4'))#Para escrever mais de uma linha

    arquivo.seek(0, 0)#Para mover o cursor para o inicio do arquivo
    print(arquivo.read())#Aqui está lendo todo o arquivo
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline())#Está lendo linha por linha
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline())
    print('Readlines')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('-' * 50)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
