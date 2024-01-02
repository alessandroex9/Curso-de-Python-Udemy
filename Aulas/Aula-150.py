"""
--Parte dois--
Try, except, else e finally
"""

try:
    a = 18
    b = 0
    print('Linha 1')
    c = a /b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
# Caso você tratar mais de um erro ne uma except
# Mais é bom você dividir os erros em except diferentes
except (NameError, IndexError) as error: 
    print('Erro:', error)
    print('Nome:', error.__class__.__name__)

except Exception: #Use caso você queira tratar qualquer erro
    print('Erro desconhecido')

print('Continuar')