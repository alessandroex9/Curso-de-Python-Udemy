"""
Faça um progrma q2ue pergunte a horta ao usuário e, baseando-se no hórario
descrito, exiba aa saudaação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_usuario = input('Que Hora é Agora: ')

try:
    hora_usuario_float = float(hora_usuario)
    if hora_usuario_float >= 0 and hora_usuario_float <= 11:
        print('Bom Dia!')
    elif hora_usuario_float >= 12 and hora_usuario_float <= 17:
        print('Boa Tarde!')
    elif hora_usuario_float >= 18 and hora_usuario_float <= 23:
        print('Boa Noite!')
    else:
        print('Não conheço essa hora!')
except: 
    print('A hora que vc digitou não é um valor válido!')