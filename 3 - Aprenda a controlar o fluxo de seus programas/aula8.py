## Loop Aninhados - Nested Loops

#ex: pais + Estação

paises =['Brasil', 'India', 'Estados Unidos']
estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']

for pais in paises:
    for estacao in estacoes:
        print(f'{pais} {estacao}')

for x in range(1, 11):
    for y in range(1, 6):
        print(f'valor interno {x} e externo {y}')