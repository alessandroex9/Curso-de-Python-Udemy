"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
continue -> Para o laço na parte do continue e volta para o começo
"""
contador = 0 
while contador <= 100:
    contador += 1

    if contador >= 6 and contador <= 10:
        print('Pular')
        continue
    print(contador)
    if contador == 50:
        
        break

print('Fim!!!')

