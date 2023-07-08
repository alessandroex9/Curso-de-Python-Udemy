# Exercicios de if e comparação
primeiro_valor = input('Digite o Primeiro valor: ') 
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor= } e maior que o {segundo_valor= }')
elif primeiro_valor < segundo_valor:
    print(f'O {segundo_valor= } e maior que o {primeiro_valor= }')
elif primeiro_valor == segundo_valor:
    print(f'O {primeiro_valor= } e o {segundo_valor= } são iguais')
else:
    print('ERRO')
