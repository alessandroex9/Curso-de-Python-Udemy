import sys #Uma biblioteca que tem uma função que mostra quantos bytes tem uma variavel
"""
Generator expression, Iterables e Iterators em Python
"""
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()# tem __iter__e__next__

# O generator é algo exclusivo do Python

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

"""
a diferença de tamanho se da por que a lista está todo na 
memoria o generator ele está pausado no primeiro item
esperando você chamar o proximo item.
"""
"""
A vantagem da lista sobre o generetor e que como ela está todo na memoria
você consegue acessar indice por indice.

Já o generetor ele economiza memoria como ele não todo salvo na memoria.
"""