"""
Calculo do Segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
mais o primeiro digito,
multiplicando cada um dos valores por uma
contagem regresiva começando de 11

Ex.: 746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <--- Primeiro Dígito
   77  40 54 64 14 24 40 34 0  14

Somar todos os resultados:
77+40+54+64+14+24+40+34+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11 
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
print('Validador de CPF')

while True:
    print("Digite seu CPF com os '.' e o '-' ")
    cpf_enviado_usuario = input('CPF: ')

    if len(cpf_enviado_usuario) != 14 or '-' not in cpf_enviado_usuario or '.' not in cpf_enviado_usuario:
         print('CPF Incorreto!')
         print('Tente de novo!')
         continue

    # Tratando o CPF
    cpf_formatado_sem_ponto = cpf_enviado_usuario.replace('.', '')
    cpf_formatado_total = cpf_formatado_sem_ponto.replace('-', '')
    
    #Pegando os noves primeiros digitos
    nove_digitos = cpf_formatado_total[:9]

    #Multiplicando e somando os 9 primeiros dígitos do CPF
    contador_regresivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regresivo_1
        contador_regresivo_1 -= 1

    # Calculando o Primeiro dígito
    digito_1 = (resultado_1 * 10) % 11
    
    #Validando o resultado
    digito_1 = digito_1 if digito_1 <= 9 else 0

    """-------- Calculo do segundo Digito ----------"""
    
    # Pegando os dez primeiros dígitos
    dez_digitos = cpf_formatado_total[:9] + str(digito_1)

    #Multiplicando e somando os dez primeiros dígitos do CPF
    contador_regresivo_2 = 11
    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regresivo_2
        contador_regresivo_2 -= 1

    #Calculando o Segundo dígito
    digito_2 = (resultado_2 * 10) % 11

    #Validando o segundo dígito
    digito_2 = digito_2 if digito_2 <= 9 else 0

    #Validação de CPF inteiro

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    
    if cpf_gerado_pelo_calculo == cpf_formatado_total:
        print('Seu CPF é valido!')
    else:
        print('Seu CPF é Inválido!')
    break