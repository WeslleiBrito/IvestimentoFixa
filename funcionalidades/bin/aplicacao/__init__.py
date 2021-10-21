from funcionalidades.bin import interface
from funcionalidades.bin import verificadores

tamanho = len(interface.investimento)


def escolha(msg):
    while True:
        investimento = verificadores.leiaint(msg)
        if 1 < investimento <= tamanho:
            return investimento
        else:
            print(f'\033[1;31mSua escolha deve ser entre 1 a {tamanho}.\033[0m')

