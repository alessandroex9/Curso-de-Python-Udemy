nome = 'Alessando'
altura = 1.70
peso = 69
imc = peso / (altura * altura)
#Como formatar strings (f-strings)
texto = f'O {nome} Tem de {altura:.2f} Pesa {peso} quilos e seu IMC é :{imc:.2f}'

print(texto)