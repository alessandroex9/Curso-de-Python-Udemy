"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(args)
        resultado = func(*args, **kwargs)

        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(param):
   if not isinstance(param, str):
       raise TypeError('param deve ser uma string')

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida1 = inverte_string('Luiz')
invertida2 = inverte_string('123')
print(invertida1)
print(invertida2)