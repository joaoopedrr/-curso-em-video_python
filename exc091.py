from random import randint
from time import sleep
from operator import itemgetter
jogo={"jogador1": randint(1, 6),
      "jogador2": randint(1, 6),
      "jogador3": randint(1, 6),
      "jogador4": randint(1, 6)}
ranking=[]
print("Valores sorteados:")
for k, v in jogo.items():
    print("{} tirou {} no dado".format(k, v))
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-="*30)
print("  == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print("  {}º lugar: {} com {}".format(i+1, v[0], v[1]))
    sleep(1)



