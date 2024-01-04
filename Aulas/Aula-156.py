import aula_156_m

print(aula_156_m.variavel)

# Caso você queira recarregar o modulo
import importlib

for i in range(10):
    importlib.reload(aula_156_m)



print('Fim')