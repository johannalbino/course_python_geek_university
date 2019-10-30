"""
GIL - Python Global Interpreter Lock
O Python Global Interpreter Lock, ou simplesmente GIL, é um mutex(ou lock) que permite que apenas uma thread tome conta
do interpretador Python

Isso significa que somente uma thread pode estar em um estado de execução em qualquer ponto do tempo.

O impacto do GIL não é comumente visível para desenvolvedores que executam programas single-thread, mas pode ser uma
dor de cabeça para programas que precisam de tempo de resposta em códigos muli-thread.

Desde que o GIL permite apenas uma thread a ser executada, mesmo em computadores multi-threads com arquitetura
que peremite utilizar mais de um CPU ou core, o GIL tem ganhado reputação como um recurso indecente do Python

Nesta aula, iremos aprender como o GIL afeta a performance do seu programa Pyuthon e também como a gente pode mitigar
o impacto do nosso código.


"""
import sys

a = []
b = a
print(sys.getrefcount(a))
