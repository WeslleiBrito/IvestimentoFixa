from funcionalidades.bin import verificadores
from funcionalidades.bin import aplicacao

valor = verificadores.leiafloat('Quanto deseja investir? ')
formajuros = verificadores.leiaint('O juros é anual[1]  ou mensal[2]? ')
taxajuros = verificadores.leiafloat('Informe a taxa de Juros %: ')
if formajuros == 1:
    taxajuros = aplicacao.conversor(taxajuros)
    while True:
        tempoaplicacao = verificadores.leiaint('Quanto tempo pretende manter o investimento(anos): ')
        if tempoaplicacao >= 1:
            tempoaplicacao = tempoaplicacao * 12
            break
        else:
            print(f'\033[1;31mO tempo de aplicação deve ser de no mínimo 1 ano.\033[0m')
else:
    while True:
        tempoaplicacao = verificadores.leiaint('Quanto tempo pretende manter o investimento(meses): ')
        if tempoaplicacao >= 1:
            break
        else:
            print(f'\033[1;31mO tempo de aplicação deve ser de no mínimo 1 mês.\033[0m')

i = aplicacao.imposto(tempoaplicacao)
print(taxajuros)
aplicacao.calculadora(valor, taxajuros, i, tempoaplicacao)
