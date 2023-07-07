"""
Introdução ao try/except
try -> tentar executar o código
except -> Ocorrreu algum erro ao tentar executar
exemplo:
int('a')
"""
#Como tratar a entrada do úsuario
numero_str = input('Vou dobrar o número que vc digitar: ')

try: 
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número') 