# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF123456789)

nome = 'Carro'
preco = 10000.45677
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco)

print(variavel)

#Usando o Hexadecimal

print('O Hexadecimal de %d é %X' % (10000, 10000))
print('O Hexadecimal de %d é %04X' % (77, 77))