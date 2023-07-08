"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.winkipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatinpoint.html
"""
import decimal # Importando um modulo do Python de tem uma classe que se chama Decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
print(type(f'{numero_3:.2f}'))
print('-' * 25)

# A função recebe o numero no primeiro parametro e na
# segunda recebe o numero de casas decimais que vc quer que apareça
print(round(numero_3, 2))
print(type(round(numero_3, 2)))
print('-' * 25)

# A classe Decimal
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
print(type(numero_3))
print('-' * 25)

# Usando a classe Decimal com Str
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(type(numero_3))
print('-' * 25)