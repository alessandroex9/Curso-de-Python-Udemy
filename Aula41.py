"""
Iterável -> str, ranger, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

#Exemplos Parametro (Iterador) para puxar o endereço de mémoria
texto = inter('Ale')
texto = 'Ale'.__inter__()

texto = iter('Ale')
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
"""
# for letra in texto:
texto = 'Alessandro' #iterável
iterador = iter(texto) #iterador

#Exemplo de como o for funciona por baixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break