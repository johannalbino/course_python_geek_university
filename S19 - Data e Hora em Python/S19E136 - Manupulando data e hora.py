"""
Manipulando Data e Hora
Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime
import datetime

print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now())
# datetime.datetime.now (year, month, day, hour, minute, second, microsecond)
print(datetime.datetime.now().__repr__())

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16hrs
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
"""

import datetime

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))
print(evento)

#aniversario = input('Informe sua data de aniversário (dd/mm/yyyy): ')
aniversario = '17/06/1995'
aniversario = aniversario.split('/')
aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))
print(type(aniversario))
print(aniversario)

# Pegando elementos separados (data e hora)
print(aniversario.day)
print(aniversario.month)
print(aniversario.year)
print(aniversario.hour)
print(aniversario.minute)
print(aniversario.second)

