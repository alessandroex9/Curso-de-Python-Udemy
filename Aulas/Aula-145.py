"""
Generator expression, Iterables e Iterators em Python
"""
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()# tem __iter__e__next__

# O iterator não sabe nada do iteravel ele só sabe entregar o proximo valor

#Iterartors
print(next(iterator))
print(next(iterator))
print(next(iterator))