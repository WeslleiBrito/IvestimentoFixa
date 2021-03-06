from funcionalidades.bin import interface
from funcionalidades.bin import verificadores
from math import pow

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


def calculadora(valor, taxa, ir, repete, aporte):
    ip = 0
    l = 0
    ap = 0
    totalaplicado = 0
    lucrobacumulado = 0
    lucrolacumulado = 0
    inicial = valor
    interface.linha()
    print(interface.titulo)
    for c in range(0, repete):
        if c % 2 == 0:
            cores = 1
        else:
            cores = 2
        if c == 0:
            lucrob = valor * taxa
        else:
            lucrob = (valor + aporte) * taxa
        lucrobacumulado += lucrob
        lucrol = lucrob - lucrob * ir
        lucrolacumulado += lucrol
        i = lucrob * ir
        ip += lucrob * ir
        l += lucrol
        if c != 0:
            valor += lucrol + aporte
            ap += aporte
        else:
            valor += lucrol
        interface.tabela(c + 1, i, lucrob, lucrol, valor, cores)
    totalaplicado = inicial + ap
    porcentagem = l / totalaplicado * 100
    interface.linha()
    interface.resumo(inicial, taxa, ir, ip, lucrobacumulado, l, valor, ap, totalaplicado, porcentagem)


def conversor(taxa):
    f = 1 / 12
    t = (taxa / 100) + 1
    return pow(t, f) - 1
