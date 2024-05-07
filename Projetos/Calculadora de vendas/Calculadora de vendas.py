def convertor_de_moedas():
    valor = input('Qual o valor para a conversão: ')
    valor = float(valor)
    print('Qual é a moeda do valor do produto para converter para o real!')
    r = 0
    while r != 1:
        moeda = input('Dolar ou Euro: ')
        moeda = str(moeda)
        if moeda == 'Dolar':
            print('Dolar Selencionado!')
            resultado = valor * 5.00
            print('O Valor do produto convertido para o dolar: ')
            print(resultado)
            r = 1
        elif moeda == 'Euro':
            print('Euro Selencionado!')
            resultado = valor * 5.70
            print('O Valor do produto convertido para o euro: ')
            print(resultado)
            r = 1  
        else:
            print('Valor informado incorreto!')
            print('Tente de novo!')
            r = 0
    
    return resultado

print ('Software para calcular o total de vendas de peças automativas')
q = 0
while q != 1:
    print ('O valor do produto é em real sim ou nao ?')
    resposta1 = input('N ou S para resposta: ')
    if resposta1 == 'N':
        print('Valor não é em real!')
        resultado = convertor_de_moedas()
        q = 1
    elif resposta1 == 'S':
        print('Valor é em real!')
        resultado = input('Insira o valor: ')
        resultado = float(resultado)
        q = 1
    else:
        print('Resposta Incoreta!')
        print('Tente novamente!')
        q = 0      
q_produtos = input('Informa a quantidade de produto vendidos: ')
q_produtos = float(q_produtos)
print('A quantidade vendidas de produtos foi: ', q_produtos)
p = 0
while p != 1:
    print('Tera desconto no valor do pagamento?')
    t = input('S ou N : ')
    if t == 'S':
        q_produtos = float(q_produtos)
        valor_da_ven = resultado * q_produtos
        desconto = valor_da_ven * 0.05
        print('O valor do desconto será: ', desconto)
        resultado_desconto = valor_da_ven - desconto
        print('O valor da Venda é de: ', valor_da_ven)
        print('O valor da venda com desconto será de: ', resultado_desconto)
        p = 1 
    elif t == 'N':
        m = 0
        while m != 1:
            print('Tera juros no valor do pagamento?')
            l = input('S ou N: ')
            while m != 1:
                print('Terá juros no valor do pagamento?')
                l = input('S ou N: ')
                if l == 'S':
                    q_produtos = float(q_produtos)
                    valor_da_ven = resultado * q_produtos
                    juros = valor_da_ven * 0.05
                    print('O juros será de: ', juros)
                    resultado_juros = resultado + juros
                    print('O valor da venda é de: ', valor_da_ven)
                    print('O valor da venda com juros será de: ', resultado_juros)
                    m = 1
                elif l == 'N':
                    print('O valor do produto não terá nem desconto nem juros')
                    total = resultado * q_produtos
                    print('O valor do pagamento produto será de:',  total)
                    m = 1
                else:
                    print('Resposta Errada!')
                    print('Tente denovo!')
                    m = 0
        p = 1
    else:
        print('Resposta incoreta Informada!')
        print('Tente de novo!')
        p == 0

print('Fim !!!')