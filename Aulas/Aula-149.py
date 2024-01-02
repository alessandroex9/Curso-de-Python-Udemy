"""
Try, except, else e finally
"""
# Não é uma boa prática de programação usar o try, except assim
# Pois pode ser de algum erro não ser tratado
try:
    a = 18
    b = 0
    print('Linha 1')
    c = a /b
    print('Linha 2')
except:
    print('Dividiu por zero')

print('Continuar')

# Ele deve ser usado assim
try:
    a = 18
    b = 0
    print('Linha 1')
    c = a /b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')

except (NameError, IndexError): # Caso você tratar mais de um erro ne uma except
    print('Uma variavel não esta definida')
    print('Index não existe')

except Exception: #Use caso você queira tratar qualquer erro
    print('Erro desconhecido')

print('Continuar')