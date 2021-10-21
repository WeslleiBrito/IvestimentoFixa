from funcionalidades.bin import interface
from funcionalidades.bin import verificadores
vrdias = len(interface.dias)
tamanho = len(interface.investimento)


def escolhainvestimento(msg):
    while True:
        investimento = verificadores.leiaint(msg)
        if 1 <= investimento <= tamanho:
            return investimento
        else:
            print(f'\033[1;31mSua escolha deve ser entre 1 a {tamanho}.\033[0m')


def escolhaprazo(msg):
    while True:
        interface.temposaplicacao()
        tp = verificadores.leiafloat(msg)
        if 1 <= tp <= vrdias:
            return tp
        else:
            print(f'\033[1;31mSua escolha deve ser entre 1 a {vrdias}.\033[0m')


