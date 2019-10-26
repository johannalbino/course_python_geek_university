"""
Decorators (Decoradores)

O que são decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria usando "@" (Syntact Sugar / Açucar Sintatico)


/--------------------------------------------------/
/                  Function Decorator             /
--------------------------------------------------

/-------------------------------------------------------/
/ /--------------------------------------------------/ /
/ /                  Function                       / /
/ /------------------------------------------------/ /
/---------------------------------------------------/


# Decorators como funções (Sintaxe não recomendada / Sem Syntact Sugar)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um otimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) a Geek University')

educacao = seja_educado(saudacao)

educacao()

# Exemplo 2

def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntact Sugar (Recomendado)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Johann')

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir')

dormir()

"""

