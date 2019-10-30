"""
Deltas de data e hora
data_inicial = dd/mm/yyy 12:55:34.9939329
data_fim = dd/mm/yyyy 13:34:23.0948484

delta = data_fim - data_inicial


import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2020, 6, 16, 0)

tempo = aniversario - data_hoje
print(tempo)

print(f'Faltam {tempo.days} dias para o meu aniversario.')

"""

import datetime

data_compra = datetime.datetime.now()
print(data_compra)
regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento = data_compra + regra_boleto
print(vencimento)