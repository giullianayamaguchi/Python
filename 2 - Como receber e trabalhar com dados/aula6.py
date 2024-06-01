teclado = 'Teclado'

#acessar qualquer um
print(teclado[2])

#acessar ultimoc aracter 
print(teclado[-1])

#acessar letra
print(teclado.index('l'))

print(teclado[teclado.index('l')])

#mais de um
##com limite
print(teclado[0:5])

##até o final
print(teclado[0:])
print(teclado[-2:])
print(teclado[:-5])

#verificar o index para ultima occorencia 
nome = "ighor Dummond indo"
print(nome.rindex('i'))