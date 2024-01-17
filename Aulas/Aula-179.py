"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- um problema que possa ser dividido em partes menores
- um caso recursivo que resolve o pequeno problema
- um caso base que para a recursão
- fotorial - n! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.oul.com.br/matematica/fatorial.html
"""

def recursiva(inicio=0, fim=10):
    # Caso base
    if inicio >= fim:
        return fim

    #Caso recursivo
    #Contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())