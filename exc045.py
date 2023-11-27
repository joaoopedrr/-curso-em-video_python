from random import randint
from time import sleep
itens= ("Pedra", "Papel", "Tessoura")
computador=randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESSOURA
''')
jogada=int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*10)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogada]))
print("-="*10)
if computador==0:
    if jogada==0:
        print("EMPATE")
    elif jogada==1:
        print("JOGADOR VENCE")
    elif jogada==2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador==1:
    if jogada==0:
        print("COMPUTADOR VENCE")
    elif jogada==1:
        print("EMPATE")
    elif jogada==2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador==2:
    if jogada==0:
        print("JOGADOR VENCE")
    elif jogada==1:
        print("COMPUTADOR VENCE")
    elif jogada==2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")