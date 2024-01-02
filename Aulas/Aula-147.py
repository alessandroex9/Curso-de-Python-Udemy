"""
Introdução às Generator functions em Python
generator = (n for n in range(10000))
"""

#Se você colocar return na função e para o yield ela só é pausada
def generator(n=0):
    yield 1 #Pausar
    print('Continuando>>>')
    yield 2 #Pausar
    print('Mais uma...')
    yield 3 #Pausar
    print('Vou terminar')
    return "Acabou"

gen = generator(n=0)
"""
print(gen.__iter__())
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

for n in gen:
    print(n)

def gerador_de_numeros(n=0, maximum=20):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
        

funcao = gerador_de_numeros()

for n in funcao:
    for n in funcao:
        print(n)