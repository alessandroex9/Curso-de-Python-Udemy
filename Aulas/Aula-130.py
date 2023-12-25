"""
Exemplo de uso dos sets
"""

letras = set()

while True:
    letra = input('Digite uma Letra: ')
    letras.add(letra.lower())
    print(letras)
    if 'l' in letras:
        print("Você achou a letra l")
        break