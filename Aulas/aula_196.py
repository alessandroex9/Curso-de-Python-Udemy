"""
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
Posicional-only Parameters (/) - Tudo antes da barra deve
ser APENAS posicional.
PEP 570 - Python Posicional-Only Parameters
https://peps.python.org/pep-0570/
Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.
PEP 3102 - Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""
def soma(a, y, /, b):
    print(a + y + b)

soma(1, 2, 7)

soma(3, 5, b=2)


def soma1(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma1(1, 2, c=3, nome='teste')