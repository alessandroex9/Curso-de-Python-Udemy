"""
Exercícios
Crie funções que duplicam, tripicam e quadruplicam
O número recebido como parâmetro.
"""

def criar_multiplicador(multiplicador):
    def mulplicar(numero):
        return numero * multiplicador
    return mulplicar

duplicar = criar_multiplicador(2)
tripicar = criar_multiplicador(3)
quadrupicar = criar_multiplicador(4)

print(duplicar(2))
print(tripicar(2))
print(quadrupicar(2))

print(duplicar(100))
print(tripicar(100))
print(quadrupicar(100))