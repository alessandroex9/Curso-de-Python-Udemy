"""
CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if (ruim)
       <-Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 90 #local em que o carro está na estrada

RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # distância onde o radar pega

carro_passou_radar1 = velocidade > RADAR_1

car_mul_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

if carro_passou_radar1:
    print('O carro passou pelo radar 1')

if car_mul_radar_1 and carro_passou_radar1:
    print('O carro passou com a velocidade a cima da permitida')