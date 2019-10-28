"""
Escrevendo em arquivos CSV
reader() (leitor), wirter() (escritor)

writerow() -> Escreve uma linha




from csv import writer

with open('filmes.csv', 'w') as arquivo:
	escritor_csv = writer(arquivo)
	filme = None
	escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
	while filme != 'sair':
		filme = input('Informe o nome do filme:')
		if filme != 'sair':
			genero = input('Informe o gênero:')
			duracao = input('Informe a duração (em minutos):')
			escritor_csv.writerow([filme, genero, duracao])
"""
from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
	cabecalho = ['Titulo', 'Genero', 'Duração']
	escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
	escritor_csv.writeheader()
	filme = None
	while filme != 'sair':
		filme = input('Informe o nome do filme: ')
		if filme != 'sair':
			genero = input('Informe o genero:')
			duracao = input('Informe a duração (em minutos):')
			escritor_csv.writerow({'Titulo': filme, "Genero": genero, "Duração": duracao})

