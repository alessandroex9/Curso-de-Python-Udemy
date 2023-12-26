"""
Função lambda com mais complexa
"""

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(executa(lambda x, y: x + y, 2, 3))


duplica = cria_multiplicador(2)

#Não fazer isso é só exemplo (Não é uma boa prática)
duplica = executa(lambda m: lambda n: n*m,2)

print(duplica(100))

print(executa(lambda *args:sum(args), 1,2,3,4,5,6,7))