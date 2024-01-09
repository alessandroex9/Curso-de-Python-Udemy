"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções
Decoradoras são "Syntax Sugar" (Açúcar sintático)
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(args)
        resultado = func(*args, **kwargs)

        return resultado
    return interna

@criar_funcao# Syntax Sugar
def inverte_string(string):
    return string[::-1]

def e_string(param):
   if not isinstance(param, str):
       raise TypeError('param deve ser uma string')



invertida = inverte_string('123')
print(invertida)
