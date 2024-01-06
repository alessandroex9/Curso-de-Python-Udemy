"""
from aula157_package.modulo import soma_do_modulo, fala_oi
from aula157_package import modulo

print(soma_do_modulo(9, 1))

fala_oi()
"""
import aula157_package
from aula157_package import soma_do_modulo

print(aula157_package.soma_do_modulo(2, 3))