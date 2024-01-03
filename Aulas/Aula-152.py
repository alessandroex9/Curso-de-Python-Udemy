"""
Raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
"""

def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('ZeroDivisionError')
        raise
    
print(divide(8, 0))
print('_' * 50)

def divide1(n, d):
    
    if not isinstance(n, (float, int)):
        raise TypeError(
            f' {n} deve ser int ou float.'
        )
    if not isinstance(d, (float, int)):
        raise TypeError(
            f' {d} deve ser int ou float.'
        )
    nao_aceito_zero(d)
    return n / d

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você esta tentando dividir por zero')

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float'
            f'{tipo_n} enviado
            )
    raise TypeError(
        
    ) 
    return True

print(divide1(10, 0))
