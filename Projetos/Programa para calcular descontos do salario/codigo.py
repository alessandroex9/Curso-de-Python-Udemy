print('Progrma para calcular quanto Voce paga em imposto de renda, inss e sidicato')
salarioh = float(input('Digite qual o valor que voce ganha por hora: '))
horastra = float(input('Quantas horas vc trabalhou por mes: '))
salariom = float(salariom)
salariom = salarioh * horastra
print('Total de Salario bruto: ', salariom)
ir = float(ir)
ir = salariom * 0.11
print('Total de desconto de Imposto de renda: ', ir)
inss = float(inss)
inss = salariom * 0.8
print('Total de desconto de INSS: ', inss)
sindicato = float(sindicato)
sindicato = salariom * 0.5
print('Total de desconto do Sindicato: ', sindicato)
salarioliq = float(salarioliq)
salarioliq = salariom - ir - inss - sindicato
print('O salario Liquido e: ', salarioliq)