from funcionalidades.bin import verificadores
from funcionalidades.bin import aplicacao
aporte = 0
valor = verificadores.leiafloat('Valor inicial? ')
if verificadores.simnao('Aporte mensal Sim[S] ou Não[N]? ') == 'S':
    aporte = verificadores.leiafloat('Qual o valor do aporte mensal? ')
formajuros = verificadores.leiaint('O juros é anual[1]  ou mensal[2]? ')
taxajuros = verificadores.leiafloat('Informe a taxa de Juros %: ')
tempo = 0
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
            taxajuros = taxajuros / 100
            break
        else:
            print(f'\033[1;31mO tempo de aplicação deve ser de no mínimo 1 mês.\033[0m')

vence = verificadores.simnao('O papel possui vencimento Sim[S] ou Não[N]? ')
if vence == 'S':
    tempo = verificadores.leiaint('Informe o prazo do vencimento: ')
else:
    tempo = tempoaplicacao

i = aplicacao.imposto(tempo)

aplicacao.calculadora(valor, taxajuros, i, tempoaplicacao, aporte)
