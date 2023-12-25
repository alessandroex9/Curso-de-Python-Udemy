"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.html
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
Tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados
de iteráveis.
 - eles não tem índexes;
 - eles não garantem ordem;
 - eles são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard

operadores úteis:
união | (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""
print('-'*50)

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 5, 6, 7, 10}

# para unir os sets
s3 = s1 | s2
print(s3)
print('-'*50)

# Iterseção para mostrar os itens presentes nos dois sets
s4 = s1 & s2
print(s4)
print('-'*50)

# para mostrar o diferente do da esquerda 

s5 = s1 - s2
print(s5)
print('-'*50)

s6 = s2 - s1
print(s6)
print('-'*50)

# Para mostrar os que não estão em ambos
s7 = s1 ^ s2
print(s7)
print('-'*50)