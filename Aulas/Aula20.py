"""
Formatação básica de strings
s - string
d - int
f - float 
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a ___repr___ ____str___
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{6546.546454664:+,.3F}')
print(f'O hexadecimal de 1500 é {1500:04X}')