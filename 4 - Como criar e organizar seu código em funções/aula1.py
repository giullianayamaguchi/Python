##Funções 
# def nome da funcao(parametros):

def dar_boas_vindas():
    print('Bem-Vindo')

#dar_boas_vindas()

def dar_Boas_Vindas_Personalziadas(nome):
    print(f'Bem-Vindo(a) {nome}')

#dar_Boas_Vindas_Personalziadas('Giu')

def apresentar_lugar(lugar='nossa loja'):
    print(f'Conheça {lugar}')

#apresentar_lugar()
#apresentar_lugar('Disney')


def apresentar_lugar(horario_de_funcionameto, lugar='nossa loja', ):
    print(f'Conheça {lugar}, horario de funcionamento {horario_de_funcionameto}')

apresentar_lugar('06:00 as 18:00')
#apresentar_lugar('Disney')
