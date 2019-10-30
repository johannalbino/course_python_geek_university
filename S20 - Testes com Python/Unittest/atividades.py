def comer(comida, saudavel):
    if saudavel is True:
        final = 'quero manter a forma.'
    else:
        final = 'a gente só vive uma vez.'
    return f'Estou comendo {comida} porque {final}'


def dormir(horas):
    if horas > 8:
        return f'Putz! Dormir muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {horas} horas. :('


def engracado(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    else:
        return False