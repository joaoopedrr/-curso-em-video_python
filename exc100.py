from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ",end="")
    for cont in range(0, 5):
        n=randint(1, 10)
        lista.append(n)
        print("{} ".format(n), end="", flush=True)
        sleep(0.3)
    print("PRONTO!")


def somaPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma=soma+valor
    print("Somando os valores pares da lista {}, temos {}".format(lista, soma))


numeros=[]
sorteia(numeros)
somaPar(numeros)

