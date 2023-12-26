# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
print('-'*50)
a, b = pessoa.values()
print(a, b)
print('-'*50)

a, b = pessoa.items()
print(a, b)
print('-'*50)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
print('-'*50)

for chave, valor in pessoa.items():
    print(chave)
    print(valor)

#Como juntar dois dicionarios
dados_pessoa = {
    'idade': 16,
    'altura': 1.6, 
}
print('-'*50)

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print('-'*50)
#args e kwargs
#args (já vimos)
#kwargs - keyword arguments(argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
print('-'*50)

mostro_argumentos_nomeados(nome='Joana', qualquer=123)


mostro_argumentos_nomeados(**pessoa_completa)
print('-'*50)
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)