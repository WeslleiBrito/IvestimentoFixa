investimento = ('LCI', 'CDB', 'LCA', 'LC', 'CRI', 'LF', 'CRA', 'DEBENTURES NÃO INCENTIVADA', 'DEBENTURES INCENTIVADA')
dias = ['Até 6 meses', 'De 7 a 12 meses', 'De 13 a 24 meses', 'Acima de 24 meses']
titulo = f"\033[1;33m{'| Mês ':7}{'| Imposto ':11}{'| L. Bruto ':9}{'| L. Liquido ':14}{'| Acumulado |':14}\033[0m"


def tipos():
    t = "Tipos de Investimento"
    print(f'\033[1;35m{t:^72}\033[0m')
    for i, c in enumerate(investimento):

        if i % 2 == 0:
            print('\033[1;32m-\033[0m' * 72)
            print(f'\033[1;32m|\033[1;34m{i + 1: ^3}\033[1;32m|\033[1;34m{c:^30}\033[1;32m|\033[0m', end='')
        else:
            print(f'\033[1;34m{i + 1:^3}\033[1;32m|\033[1;34m{c:^31}', end='\033[1;32m|\033[0m\n')

    if len(investimento) % 2 != 0:
        print()
        print('{:68}'.format('\033[1;32m-\033[0m' * 36))


def temposaplicacao():
    for i, d in enumerate(dias):
        print(f'{"-" * 21}')
        print(f'{i + 1:<1} - {d:^21}')


def linha():
    print('-' * 56)


def tabela(num=0, ir=0, lucrobruto=0, lucroliquido=0, acumulado=0, cor=0):
    ir = str(f'{ir:.2f}').replace('.', ',')
    lucrobruto = str(f'{lucrobruto:.2f}').replace('.', ',')
    lucroliquido = str(f'{lucroliquido:.2f}').replace('.', ',')
    acumulado = str(f'{acumulado:.2f}').replace('.', ',')
    if cor == 1:
        print(f'\033[1;30;46m|{num:^6}|{ir:^10}|{lucrobruto:^10}|{lucroliquido:^13}|{acumulado:^11}|\033[0m')
    else:
        print(f'\033[1;30;44m|{num:^6}|{ir:^10}|{lucrobruto:^10}|{lucroliquido:^13}|{acumulado:^11}|\033[0m')


def resumo(inicial, taxajuros, i, ir, lucrobruto, lucroliquido, montante, aportes, total, p):
    p = str(f'{p:.2f}').replace('.', ',')
    total = str(f'{total:.2f}').replace('.', ',')
    aportes = str(f'{aportes:.2f}').replace('.', ',')
    inicial = str(f'{inicial:.2f}').replace('.', ',')
    taxajuros = taxajuros * 100
    taxajuros = str(f'{taxajuros:.2f}').replace('.', ',')
    i = str(f'{i * 100:.2f}').replace('.', ',')
    ir = str(f'{ir:.2f}').replace('.', ',')
    lucrobruto = str(f'{lucrobruto:.2f}').replace('.', ',')
    lucroliquido = str(f'{lucroliquido:.2f}').replace('.', ',')
    montante = str(f'{montante:.2f}').replace('.', ',')
    print(f'{"Valor Inicial R$:":<22}{inicial:>10}')
    print(f'{"Aportes mensais R$:":<22}{aportes:>10}')
    print(f'{"Taxa de Juros %a.m:":<22}{taxajuros:>10}')
    print(f'{"Imposto de Renda %:":<22}{i:>10}')
    print(f'{"Imposto de Renda R$:":<22}{ir:>10}')
    print(f'{"Lucro Bruto R$:":<22}{lucrobruto:>10}')
    print(f'{"Lucro Líquido R$:":<22}{lucroliquido:>10}')
    print(f'{"Total Aplicado R$:":<22}{total:>10}')
    print(f'{"Montante R$:":<22}{montante:>10}')
    print(f'{"Lucro %:":<22}{p:>10}')


