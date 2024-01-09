"""
Exercicio - Unir listas
Crie uma função zipper (como o zipper de roupas)
o trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Hizonte', 'MG')]
"""

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

def parametros_decorador():
    def decorador(func):
        lista_agregada = [None]
        def sua_nova_funcao(*args, **kwargs):           
            nonlocal lista_agregada
            i = 0
            while i >= len(cidade):
                lista_agregada = cidade[::i] + estado[::i]
            return lista_agregada
        return sua_nova_funcao
    return decorador



