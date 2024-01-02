"""
dir, hasattr e getattr em Python
"""
string = 'Alessandro'

#Para saber os metodos disponiveis em qualquer variavel
#E só colocar dir() no console do debug para ser mostrado os metodos

#hasattr checa se um determinado objeto tem determinado metodo
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())
    print('-'* 50)

# Fazendo hasattr dinamicamente
metodo = 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())