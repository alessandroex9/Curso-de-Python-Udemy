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
# Para ter um limite de recursão maior que 1000(Padrão Python)
import sys
sys.setrecursionlimit(1005)

def recursiva(inicio=0, fim=4):
    print(inicio,fim)

    #caso base
    if inicio >= fim:
        return fim
    
    #caso recursivo
    #contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva(0, 996))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(20))
