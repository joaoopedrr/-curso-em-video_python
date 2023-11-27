from time import sleep
n1=int(input("Primeiro valor:"))
n2=int(input("Segundo valor:"))
opçao=0
while opçao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opçao=int(input("Qual é a sua opção:"))
    if opçao==1:
        soma=n1+n2
        print("A soma de {} + {} é igual a {}".format(n1, n2, soma))
    elif opçao==2:
        multiplicaçao=n1*n2
        print("A multiplicação de {} x {} é igual a {}".format(n1, n2, multiplicaçao))
    elif opçao==3:
        if n1>n2:
            maior=n1
        elif n1<n2:
            maior=n2
        else:
            print("Os números são iguais!")
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
    elif opçao==4:
        print("Informe os números novamente.")
        n1=int(input("Primeiro valor:"))
        n2=int(input("Segundo valor:"))
    elif opçao==5:
        print("Finalizando...")
    else:
        print("Opção inválida, tente novamente!")
    print("=-=" *10)
    sleep(2)
print("Fim do programa! Volte sempre!")
