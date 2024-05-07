def calcular(valor1):
    i = 1
    while i != 0:
        operador = input('Insira o operador: ')
        if operador == '+':
            valor2 = int(input('Insira o segundo Valor: '))
            resultado = valor1 + valor2
            print('O resultado do Cálculo: ', resultado)
            i = 0
        elif operador == '-':
            valor2 = int(input('Insira o Segundo valor: '))
            resultado = valor1 - valor2
            print('O resultado do Cálculo', resultado)
            i = 0
        elif operador == '*':
            valor2 = int(input('Insira o Segundo valor: '))
            resultado = valor1 * valor2
            print('O resultado do Cálculo', resultado)
            i = 0
        elif operador == '/':
            valor2 = int(input('Insira o Segundo valor: '))
            resultado = valor1 / valor2
            print('O resultado do Cálculo', resultado)
            i = 0
        else:
            print('Operador Invalido!')
            i = 1
    return resultado

print('Seja Bem-Vindo a Calculadora')
try:
    valor1 = int(input('Insira o primeiro valor: '))
calcular()
resultado = calcular()
print('O valor do calculo: ', resultado)
print('FIM!!!')