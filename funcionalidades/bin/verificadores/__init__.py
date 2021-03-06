def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print(f'\033[1;31mInforme apenas números, tente novamente.\033[0m')
        else:
            return int(n)


def leiafloat(msg):
    while True:
        try:
            valor = str(input(msg))
            vr = valor.replace(',', '.', 1)
            vr = float(vr)
        except (ValueError, TypeError):
            print(f'\033[1;31mInforme o valor valido, tente novamente.\033[m')
        else:
            return float(vr)


def simnao(msg):
    while True:
        try:
            letra = str(input(msg).upper()[0])
        except:
            print('\033[1;31mInforme [N] Não ou [S] Sim.\033[0m')
        else:
            if letra in 'NS':
                if letra == 'S':
                    return letra
                else:
                    return 1
