from time import sleep

def contador(i, f, g):
    if g < 0:
        g=g*-1
    if g == 0:
        g=1
    print("Contagem de {} até {} de {} em {}".format(i, f, g, g))
    sleep(2)

    if i < f:
        cont=i
        while cont <= f:
            print("{}  ".format(cont), end="", flush=True)
            sleep(0.5)
            cont=cont+g
        print("FIM!")
    else:
        cont=i
        while cont >= f:
            print("{}  ".format(cont), end="", flush=True)
            sleep(0.5)
            cont=cont-g
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
inicio=int(input("Início: "))
fim=int(input("Fim: "))
passo=int(input("Passo: "))
contador(inicio, fim, passo)

