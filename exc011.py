largura=float(input("Qual é a largura em metros dessa parede:"))
altura=float(input("Qual é a altura em metros dessa parede:"))
area=largura*altura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(largura, altura, area))
tinta=area/2
print("A quantidade necessária para limpar a parede é de {} litros de tinta".format(tinta))