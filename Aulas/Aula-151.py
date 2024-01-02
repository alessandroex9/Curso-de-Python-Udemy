"""
Try, except, else e finally
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
"""
try:
    print('Try')
    8/0

except ZeroDivisionError:
    print('Divisão por zero')

else: #Vai ser executado caso não ocorra erro
    print('Não teve erro')

# ocorra oque ocorrer o finaly sempre será executado  
finally:
    print('Finally')