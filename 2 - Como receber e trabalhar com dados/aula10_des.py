# DESAFIO 🥇
# Calcule quantos dias faltam até o seu aniversário
from datetime import datetime

data_aniversario = datetime(2025, 1, 30)
dias = data_aniversario - datetime.now()
print('  ')
print(dias)