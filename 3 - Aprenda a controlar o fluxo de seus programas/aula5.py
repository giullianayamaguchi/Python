#if elif else

trabalho_terminado = True

if trabalho_terminado == True: 
    print('Bora sair')
else:
    print('Vou terminar meu trabalho primeiro')


numero_atraso = 2

if numero_atraso >= 3:
    print('Vá para diretoria')
elif numero_atraso == 2:
    print('Essa é sua segunda falta')
elif numero_atraso == 1:
    print('Essa é sua primeira falta')
else:
    print('pode entrar')



velocidade_maxima = 50

if velocidade_maxima < 50: 
    print('nçao foi multado')
elif velocidade_maxima >= 51 and velocidade_maxima <= 60:
    print('Você levou 2 pontos de multa')
elif 51 <= velocidade_maxima <= 60:
    print("levou 3 pontos")
else:
    print('levou multa de 7 pontos')

