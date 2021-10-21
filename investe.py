from funcionalidades.bin import verificadores
from funcionalidades.bin import aplicacao
from funcionalidades.bin import interface

valor = verificadores.leiafloat('Quanto deseja investir? ')
taxajuros = verificadores.leiafloat('Informe a taxa de Juros %: ')
vencimento = verificadores.simnao('O papel possui vencimento [S] sim ou [N] não: ')
if vencimento == 'S':
    prazo = verificadores.leiaint('O papel vence em quantos meses: ')
else:
    prazo = vencimento


interface.tipos()


