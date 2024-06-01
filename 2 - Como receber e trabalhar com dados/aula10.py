#data e time

from datetime import datetime

#pegar data e hora atual
print(datetime.now())

#pegar inmformação especifica
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#crair uma data
lancamento = datetime(2021,5,25)
print(lancamento)

#quero receber a data
data = datetime.strptime(input("quando devemos lançar: "),'%d/%m/%Y')
print(data)


#COMPARAR DATAS
data_atual = datetime.now()
data_lancamento = data - data_atual
print(data_lancamento.days)