

idade = 21
possui_convide = False
filho_dono = True

#obrigatoriamente 2 verdadesiras
print((idade >= 21) and (possui_convide == True))

#obrigatoriamente 1 verdadesiras
print(idade >= 21 or possui_convide == True)

#obrigatoriamente2 verdadeiros
print((idade > 21 and possui_convide == True) or (filho_dono == True))




maior_idade = True
possui_carteira = True
trabalhando = False
veiculo_proprio = False
print((maior_idade == True) and (possui_carteira == True))
print((maior_idade) and (possui_carteira))

print((possui_carteira == True) and not (veiculo_proprio))