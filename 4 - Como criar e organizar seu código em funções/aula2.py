#processar e retornar 

#funções que apenas processa dados 
print('ola')

#funções que retorna dados 
cidade = input('Qual é a cidade?')

#exemplo
def exibir_cotacao(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_cotacao('usd')

def obter_moeda(moedaa):
    if moedaa == 'usd':
        return 5.47
    

cotacao = obter_moeda('usd')
if cotacao >5:
    print('investir em ações americanas')
else: 
    print('Cotação nçao favorável')