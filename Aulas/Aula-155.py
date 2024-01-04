"""
Entendendo os seus próprios módulos python
O proimeiro ódulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O Python conhece a pasta onde o __main__ está e as pastas
abaixop dele.
Ele não reconhece pastas e módulos acima do __main__
por padrão
O python conhece  todos os módulos e pacotes presentes
nos caminhos de sys.path
"""
import aula_154_m
# Para importar só mente a variavel do modulo
from aula_154_m import variave_modulo, soma

print(aula_154_m.variave_modulo)

print(variave_modulo)

print(aula_154_m.soma(2, 2))

print(soma(3, 3))