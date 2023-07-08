"""
Flags (bandeira) - MArcar um local
Nome = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao:
    print('Faça algo')
    passou_no_if = True

else:
    print("Não faça algo")

if passou_no_if is None:
    print('Não passou no if')

else:
    print('Passou no if')

#print(passou_no_if, passou_no_if is None)
#print(passou_no_if, passou_no_if is not None)