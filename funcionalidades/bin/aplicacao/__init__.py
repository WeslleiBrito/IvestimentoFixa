from funcionalidades.bin import interface
from funcionalidades.bin import verificadores
from math import floor, pow
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


def imposto(prazo):

    if prazo < 6:
        return 0.225
    elif 6 < prazo <= 12:
        return 0.2
    elif 12 < prazo <= 24:
        return 0.175
    else:
        return 0.15


def calculadora(valor, taxa, ir, repete):

    for c in range(0, repete):
        lucrob = valor * (taxa / 100)
        lucrol = floor(lucrob - lucrob * ir)
        valor += lucrol

    print(f'Montante: {valor}')


def conversor(taxa):
    return pow((1 + (taxa/100)), 12) - 1



