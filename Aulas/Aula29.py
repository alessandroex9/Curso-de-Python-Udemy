"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Alessandro'
"""
string[3] = 'B'
Não consigo fazer essa atribuição por se tratar
de váriavel imutável
"""
#Agora um exemplo de como fazer a atribuição de uma váriavel imutável
outra_variavel = f'{string[:3]}B{string[4:]}'

print(outra_variavel)