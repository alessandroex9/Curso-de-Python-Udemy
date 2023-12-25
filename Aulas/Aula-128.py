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

s1 = set()
#O add só aceita um valor por vez
s1.add('Alessandro')
s1.add(10)
print(s1)
print('-'*50)

#O update é quase igual o add só ele vai ser de forma interada
s1.update('Martins')
print(s1)
print('-'*50)
#Para passar valor com update de forma interavel
#O update da para passar varios valores juntos
s1.update(('Santos', 'dos'))
print(s1)
print('-'*50)

#Para limpar o set se usa o clear
s1.clear()
print(s1)
print('-'*50)
s1 = set('Parei')
s1.update('teclado')
print(s1)
print('-'*50)

# O comando discard serve para eliminar valores
s1.discard('Parei')
print(s1)
print('-'*50)