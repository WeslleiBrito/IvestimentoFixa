from funcionalidades.bin import verificadores
from funcionalidades.bin import aplicacao
from funcionalidades.bin import interface
vencimento = verificadores.simnao('O papel tem vencimento [S]/[N]? ')
if vencimento == 'S':
    prazo = verificadores.leiafloat('Vencimento do papel em meses: ')
else:
    prazo = vencimento
verificadores.leiaint('Informe o número de meses da aplicação: ')
verificadores.leiafloat('Informe a taxa de Juros %: ')
interface.tipos()


