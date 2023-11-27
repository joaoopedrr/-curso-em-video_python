def aumentar(preço, taxa):
    resp= preço + (preço * taxa/100)
    return resp


def diminuir(preço, taxa):
    resp= preço-(preço * taxa/100)
    return resp


def dobro(n):
    d=n*2
    return d


def metade(n):
    m=n/2
    return m

