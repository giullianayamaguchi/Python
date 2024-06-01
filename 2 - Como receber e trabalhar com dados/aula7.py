frase = 'olá, bem vindo a este treinamento'

#separar em listar por espaço
print(frase.split())

#separa por caracter
print(frase.split(','))

hashtags = 'music #guitar #gamer #coder #python'

#separar por caracter limitando 
print(hashtags.split('#', 3))

#juntar strings

separar = hashtags.split()
print(separar)

print('.'.join(separar))