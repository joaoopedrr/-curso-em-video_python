from random import randint
from time import sleep
computador=randint(0,5)
print("--"*10)
print("Vou pensar em um número de 0 a 5, tente adivinhar!")
print("--"*10)
jogador=int(input("Em que número eu pensei?"))
print("Processando...")
sleep(2)
if jogador==computador:
    print("Parabéns! você conseguiu me vencer!")
else:
    print("Você perdeu, eu pensei no número {} e não no {}".format(computador,jogador))