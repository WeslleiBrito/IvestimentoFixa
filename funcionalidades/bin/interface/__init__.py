investimento = ('LCI', 'CDB', 'LCA', 'LC', 'CRI', 'LF', 'CRA', 'DEBENTURES NÃO INCENTIVADA', 'DEBENTURES INCENTIVADA')


def tipos():
    print()
    for i, c in enumerate(investimento):

        if i % 2 == 0:
            print('\033[1;32m-\033[0m' * 72)
            print(f'\033[1;32m|\033[1;34m{i + 1: ^3}\033[1;32m|\033[1;34m{c:^30}\033[1;32m|\033[0m', end='')
        else:
            print(f'\033[1;34m{i + 1:^3}\033[1;32m|\033[1;34m{c:^31}', end='\033[1;32m|\033[0m\n')

    if len(investimento) % 2 != 0:
        print()
        print('{:68}'.format('\033[1;32m-\033[0m' * 36))


