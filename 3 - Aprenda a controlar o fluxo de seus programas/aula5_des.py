#Desafio 🥇

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

'''

Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
'''

tamanho = 32

if  tamanho <= 20:
    print('valor 20,00')
elif 21 <= tamanho <= 30:
    print('valor 70,00')
elif 31 <= tamanho <= 50:
    print('Valor 100,00')
else: 
    print('Favor consultar na recepção')