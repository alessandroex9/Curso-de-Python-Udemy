"""
Gerador de CPFs
"""
import random
print('Gerador de CPFs')

while True:

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))



    # Multiplicando e somando os 9 primeiros dígitos do CPF
    contador_regresivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regresivo_1
        contador_regresivo_1 -= 1

    # Calculando o Primeiro dígito
    digito_1 = (resultado_1 * 10) % 11
    
    # Validando o resultado
    digito_1 = digito_1 if digito_1 <= 9 else 0

    """-------- Calculo do segundo Digito ----------"""
    
    # Pegando os dez primeiros dígitos
    dez_digitos = nove_digitos[:9] + str(digito_1)

    # Multiplicando e somando os dez primeiros dígitos do CPF
    contador_regresivo_2 = 11
    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regresivo_2
        contador_regresivo_2 -= 1

    # Calculando o Segundo dígito
    digito_2 = (resultado_2 * 10) % 11

    # Validando o segundo dígito
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Validação de CPF inteiro

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(f'CPF Gerado: {cpf_gerado_pelo_calculo}')
    break