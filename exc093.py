jogador={}
partidas=[]
jogador["nome"]=str(input("Nome do jogador: "))
tot=int(input("Quantas partidas {} jogou? ".format(jogador["nome"])))
for c in range(0, tot):
    partidas.append(int(input("    Quantos gols na partida {}:".format(c+1))))
jogador["gols"]=partidas[:]
jogador["total"]=sum(partidas)
print("-="*30)
print(jogador)
print("-="*30)
for k, v in jogador.items():
    print("   |O campo {} tem o valor: {}".format(k, v))
print("-="*30)
print("O jogador {} jogou {} partidas".format(jogador["nome"], len(jogador["gols"])))
for i, v in enumerate(jogador["gols"]):
    print("   => Na partida {}, fez {} gols".format(i+1, v))
print("Foi um total de {} gols.".format(jogador["total"]))



