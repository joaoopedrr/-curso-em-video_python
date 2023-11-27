def aumentar(preço=0, taxa=0, formatado=False):
    resp= preço + (preço * taxa/100)
    return resp if formatado is False else moeda(resp)


def diminuir(preço=0, taxa=0, formatado=False):
    resp= preço-(preço * taxa/100)
    return resp if formatado is False else moeda(resp)


def dobro(n=0, formatado=False):
    d=n*2
    return d if formatado is False else moeda(d)


def metade(n=0, formatado=False):
    m=n/2
    return m if formatado is False else moeda(m)


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:.2f}".replace(".", ",")


def resumo(preço=0, taxaa=10, taxaar=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print("Preço analisado: \t{}".format(moeda(preço)))
    print("Dobro do preço: \t{}".format(dobro(preço, True)))
    print("Metade do preço: \t{}".format(metade(preço, True)))
    print("{}% de aumento: \t{}".format(taxaa, aumentar(preço, taxaa, True)))
    print("{}% de redução: \t\t{}".format(taxaar, diminuir(preço, taxaar, True)))
    print("-"*30)




