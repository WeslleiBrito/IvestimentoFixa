investimento = ('LCI', 'CDB', 'LCA', 'LC', 'CRI', 'LF', 'CRA', 'DEBENTURES NÃO INCENTIVADA', 'DEBENTURES INCENTIVADA')
dias = ['Até 6 meses', 'De 7 a 12 meses', 'De 13 a 24 meses', 'Acima de 24 meses']
titulo = f"{'| Mês ':7}{'| Imposto ':11}{'| L. Bruto ':9}{'| L. Liquido ':14}{'| Acumulado |':14}"


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
    linha()
    # print(f"{'| Mês ':7}{'| Imposto ':11}{'| L. Bruto ':9}{'| L. Liquido ':14}{'| Acumulado |':14}")
    if cor == 1:
        print('\033[1;30;42m|{:^6}|{:^10.2f}|{:^10.2f}|{:^13.2f}|{:^11.2f}|\033[0m'.format(num, ir, lucrobruto,
                                                                                           lucroliquido, acumulado))
    elif cor == 2:
        print('\033[1;30;44m|{:^6}|{:^10.2f}|{:^10.2f}|{:^13.2f}|{:^11.2f}|\033[0m'.format(num, ir, lucrobruto,
                                                                                           lucroliquido, acumulado))
    else:
        print('|{:^6}|{:^10.2f}|{:^10.2f}|{:^13.2f}|{:^11.2f}|'.format(num, ir, lucrobruto, lucroliquido, acumulado))
