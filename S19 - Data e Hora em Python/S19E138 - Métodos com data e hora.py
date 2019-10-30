"""
Métodos com data e hora.


import datetime

# Com now() podemos especificar um timezone(Fuso Horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

# Com today() não podemos especificar uma timezone
hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

import datetime

# Mudanças ocorrendo á meia-noite

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)



import datetime

# Encontrar o dia da semana com weekday()
# 0 - Monday (Segunda) 1 - Tuesday (Terça) 2 - Wednesday (Quarta) 3 - Thursday (Quinta) 4 - Friday (Sexta) 5 - Sathurday
# (Sabado) 6 - Sunday (Domingo)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=2)), datetime.time())

print(manutencao.weekday())

import datetime

aniversario = input('Qual a sua data de aniversario? (dd/mm/yyyy) ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
	print('Você nasceu na segunda-feira!')
elif aniversario.weekday() == 1:
	print(f'Você nasceu na terça-feira')
elif aniversario.weekday() == 2:
	print(f'Você nasceu na quarta-feira')
elif aniversario.weekday() == 3:
	print(f'Você nasceu na quinta-feira')
elif aniversario.weekday() == 4:
	print(f'Você nasceu na sexta-feira')
elif aniversario.weekday() == 5:
	print(f'Você nasceu no sabado')
elif aniversario.weekday() == 6:
	print(f'Você nasceu no domingo')

days = ['Você nasceu na segunda', 'Você nasceu na terça', 'Você nasceu na quarta', 'Você nasceu na quinta',
		'Você nasceu na sexta', 'Você nasceu no sabado', 'Você nasceu no domingo']

print(days[aniversario.weekday()])


import datetime

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%B/%Y')
print(hoje_formatado)

import datetime
from textblob import TextBlob

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto


def format_date(data):
	date = (f'{data.day} de Janeiro de {data.year}', f'{data.day} de Fevereiro de {data.year}',
			f'{data.day} de Março de {data.year}', f'{data.day} de Abril de {data.year}',
			f'{data.day} de Maio de {data.year}', f'{data.day} de Junho de {data.year}',
			f'{data.day} de Julho de {data.year}', f'{data.day} de Agosto de {data.year}',
			f'{data.day} de Setembro de {data.year}', f'{data.day} de Outubro de {data.year}',
			f'{data.day} de Novembro de {data.year}', f'{data.day} de Dezembro de {data.year}')

	return date[data.month - 1]


def format_date2(data):
	return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()
print(format_date(hoje))
print(format_date2(hoje))

print(TextBlob('I never use a dictionary').translate(to='pt-br'))

import datetime

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)

import datetime

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)

import timeit

# Marcando tempo de execucao do nosso código com timeit

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
"""
import timeit, functools


def teste(n):
	soma = 0
	for num in range(n * 200):
		soma = soma + num ** num +4
	return soma


print(timeit.timeit((functools.partial(teste, 2)), number=10000))
