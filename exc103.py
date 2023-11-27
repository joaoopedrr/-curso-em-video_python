def ficha(jog="<desconhecido>", gol=0):
    print("O jogador {} fez {} gol(s) no campeonato.".format(jog, gol))


n=str(input("Qual o nome do jogador: "))
g=str(input("Quantos gols ele fez: "))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)
