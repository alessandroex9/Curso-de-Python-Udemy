""" Calculadora com while """
sair = False
while True:
  
    numero_1 = input('Digite o primeiro digito: ')
    numero_2 = input('Digite o segundo digito: ')
    operador = input('Digite um operador (+, -, /, *): ')
    
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0 

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2) 
        numeros_validos = True
    
    except:
        numeros_validos = None
        
    if numeros_validos is None:   
        print('UM ou ambos Números São inválidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Inválido!')
        continue

    if len(operador) > 1:
        print('Quantidade não permitida!')
        print('Digite apenas um operador!')
        continue
    
    print('Realizando sua conta. Confira seu resultado abaixo:')

    if operador == '+':
        print(numero_1_float + numero_2_float)

    elif operador == '-':
        print(numero_1_float - numero_2_float)

    elif operador == '*':
        print(numero_1_float * numero_2_float)
        
    elif operador == '/':
        print(numero_1_float / numero_2_float)

    else:
        print('Nunca Deveria chegar aqui!') 

    sair = input('Quer sair? \n [s]').lower().startswith('s')

    if sair is True:
        break