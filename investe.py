from funcionalidades.bin import verificadores
from funcionalidades.bin import aplicacao

repete = 1
valor = verificadores.leiafloat('Quanto deseja investir? ')
taxajuros = verificadores.leiafloat('Informe a taxa de Juros %: ')
vencimento = verificadores.simnao('O papel possui data de vencimento [S] sim ou [N] não: ')
if vencimento == 'S':
    prazo = verificadores.leiaint('O papel vence em quantos meses: ')
    tempoaplicacao = verificadores.leiaint('Quanto tempo pretende manter o investimento(meses): ')
    i = aplicacao.imposto(prazo)
    if prazo < tempoaplicacao:
        repete = tempoaplicacao // prazo
else:
    tempoaplicacao = verificadores.leiaint('Quanto tempo pretende manter o investimento(meses): ')
    i = aplicacao.imposto(tempoaplicacao)

aplicacao.calculadora(valor, taxajuros, i, repete)
