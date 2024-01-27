"""
Problema dos parâmentros mutáveis em funções Python
"""
# Modo errado de passar parâmetros
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

print(cliente1)
print(cliente2)
print('-'* 50)

#Modo certo de passar parâmetros

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

lista1 = []# Tem que criar a lista pois ela não é cria na função
cliente1 = adiciona_clientes('Luiz', lista1)
adiciona_clientes('Joana', cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

print(cliente1)
print(cliente2)
print('-'* 50)

# Mais a forma mais correta é não usar parâmetros mutáveis em chamadas de função

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []

    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Alessandro')
adiciona_clientes('Jorge', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('João')
adiciona_clientes('Mario', cliente2)
print(cliente2)