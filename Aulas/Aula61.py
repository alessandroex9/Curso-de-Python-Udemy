"""
Calculo do Primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regresiva começando de 10

Ex.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11 
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Código validador de CPF

print('Validador de CPF')

while True:
    print("Digite seu CPF com os '.' e o '-' ")
    cpf = input('CPF: ')

    if len(cpf) != 14 or '-' not in cpf or '.' not in cpf:
         print('CPF Incorreto!')
         print('Tente de novo!')
         continue

    # Tratando o CPF
    cpf_formatado_sem_ponto = cpf.replace('.', '')
    cpf_formatado_total = cpf_formatado_sem_ponto.replace('-', '')
    
    #Pegando os noves primeiros digitos e transformando em int
    nove_digitos = cpf_formatado_total[:9]
    #nove_digitos_int = int(nove_digitos)

    #Multiplicando e soma dos 9 primeiros dígitos do CPF
    contador_regresivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regresivo_1
        contador_regresivo_1 -= 1

    # Calculando o Primeiro Digito
    digito_1 = (resultado_1 * 10) % 11
    
    #Validando o resultado
    digito_1 = digito_1 if digito_1 <= 9 else 0

    if digito_1 == cpf_formatado_total[9]:
        print('CPF Válido!')
    else:
        print('CPF Inválido!')

    break