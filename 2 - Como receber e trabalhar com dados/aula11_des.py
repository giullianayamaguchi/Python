# DESAFIO 🥇

'''
# Desafios Random 
1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
    jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
    Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
3. você quer escolher aleatóriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100
    '''
import random

print('\n 1 \n')
moeda = ['cara', 'coroa']
print(random.choice(moeda))

print('\n 2 \n')
nomes = ['Ighor', 'Giulliana', 'Carlos', 'Vera', 'Daniel']
print(random.choice(nomes))

print('\n 3 \n')
print(random.randint(10, 100))
