def aumentar(preço=0, taxa=0):
    resp= preço + (preço * taxa/100)
    return resp


def diminuir(preço=0, taxa=0):
    resp= preço-(preço * taxa/100)
    return resp


def dobro(n=0):
    d=n*2
    return d


def metade(n=0):
    m=n/2
    return m


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:.2f}".replace(".", ",")






