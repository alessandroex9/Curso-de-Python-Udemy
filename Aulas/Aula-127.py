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

s1 = {1, 1, 2, 3, 3, 3, 3, 3, 2}
# Os sets eliminam os valores duplicados
print(s1)

s2 = set('Alessandro')
# os sets alem de eliminar os repitidos não garante a ordem

print(s2)
print(s2)
print(s2)

#Ele vai matar os dados repetidos e não vai aparecer em ordem
for letras in s2:
    print(letras)