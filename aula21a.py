'''def contador(i, f, g):
    c=i
    while c <= f:
        print("{} ".format(c), end="")
        c=c+g
    print("FIM!")


contador(1, 10, 1)'''






'''def contador(i, f, g):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param g: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara CursoemVideo.
    """
    c=i
    while c <= f:
        print("{} ".format(c), end="")
        c=c+g
    print("FIM!")


help(contador)'''






'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """
    s=a+b+c
    print("A soma vale {}".format(s))


somar(3, 6)'''




'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """
    s=a+b+c
    print("A soma vale {}".format(s))


somar(3)'''



'''def teste():
    x=8
    print("Na função teste, n vale {}".format(n))
    print("Na função teste, x vale {}".format(x))


#Programa principal
n=2
print("No programa principal, n vale {}".format(n))
teste()
print("No programa principal, x vale {}".format(x))'''





'''def teste(b):
    a=8
    b=b+4
    c=2
    print("A dentro vale {}".format(a))
    print("B dentro vale {}".format(b))
    print("C dentro vale {}".format(c))


a=5
teste(a)
print("A fora vale {}".format(a))'''





'''def teste(b):
    global a
    a=8
    b=b+4
    c=2
    print("A dentro vale {}".format(a))
    print("B dentro vale {}".format(b))
    print("C dentro vale {}".format(c))


a=5
teste(a)
print("A fora vale {}".format(a))'''






'''def somar(a=0, b=0, c=0):
    s=a+b+c
    print("A soma vale {}".format(s))


somar(3, 2, 1)
somar(2, 2)
somar(5)'''


'''def somar(a=0, b=0, c=0):
    s=a+b+c
    return s


resp1=somar(3, 2, 1)
resp2=somar(2, 2)
resp3=somar(5)

print("Os resultados foram {}, {} e {}".format(resp1, resp2, resp3))'''




'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num=int(input("Digite um número: "))
print(par(num))'''




def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num=int(input("Digite um número: "))
if par(num):
    print("É par!")
else:
    print("É ímpar!")







