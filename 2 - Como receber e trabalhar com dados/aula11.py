#valores aleatórios com random

import random

#gerar valor aleatorio de 0,0  a 1,0
print(random.random())

#gerar decimal de 4 a 10
print(random.uniform(4, 10))

#gerar inteiro de 4 a 10
print(random.randint(4, 10))


cores = ['verde', 'vermelho', 'azul']

#uma opcao
print(random.choice(cores))

#mais opcoes
print(random.choices(cores, k=2))

#embaralhar
cartas = [ 'carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas))
print(cartas)