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
import sys

import aula_154_m

print('Este módulo se chama ', __name__)

print(*sys.path, sep='\n')