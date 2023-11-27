'''def total(n1, n2):
    soma=n1+n2
    media=soma/2
    print("A sua primeira nota foi {} e a segunda foi {}, tendo ficado com a média {}.".format(n1, n2, media))

print("CALCÚLO DE MÉDIA")
print("-"*30)
nota1=float(input("Qual foi a sua primeira nota: "))
nota2=float(input("Qual foi a sua segunda nota: "))
total(nota1, nota2)'''





def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f=1
    for c in range(n, 0, -1):
        if show:
            print("{}".format(c), end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f=f*c
    return f


print(fatorial(5, show=True))
help(fatorial)