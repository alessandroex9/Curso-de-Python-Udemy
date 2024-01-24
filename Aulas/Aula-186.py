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
"""
arquivo = open(caminho_arquivo, 'w')

#Sempre feche o arquivo
arquivo.close()
"""

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá')
    print('Seu arquivo vai ser fechado por causa do with')