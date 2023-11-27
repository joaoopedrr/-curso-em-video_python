from time import sleep

def maior(*num):
    cont=0
    maior=0
    print("\nAnalisando os valores passados...")
    for valor in num:
        print("{} ".format(valor), end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        cont=cont+1
    print("Foram informados {} valores ao todo".format(cont))
    print("O maior valor informado foi {}".format(maior))


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
