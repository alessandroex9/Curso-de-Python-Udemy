# OR
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# Para priorizar a condiação pode ser colocada entre ()
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
    print('Iniciano Sistema')
else:
    print('Sair')


# Avaliação de curto Circuito
print(True or False or False)
print(False or 0 or 'ABC')

# Exemplo de avaliação 
senha = input('Senha: ') or 'Sem senha'
print('senha')