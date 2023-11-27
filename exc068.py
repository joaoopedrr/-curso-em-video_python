from random import randint
v=0
while True:
    jogador=int(input("Diga um valor:"))
    computador= randint(0, 10)
    total=jogador+computador
    tipo=" "
    while tipo not in"PpIi":
        tipo=str(input("Par ou Ímpar? [P/I]")).upper().strip()[0]
    print("Você jogou {} e o computador {}. Total de {}".format(jogador, computador, total), end="    ---")
    print("|DEU PAR|" if total % 2 == 0 else "|DEU ÍMPAR|")
    if tipo=="P":
        if total % 2 == 0:
            print("Você VENCEU!")
            v= v+1
        else:
            print("Você PERDEU!")
            break
    elif tipo=="I":
        if total % 2 == 1:
            print("Você VENCEU!")
            v=v+1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print("GAME OVER! Você venceu {} vezes.".format(v))
