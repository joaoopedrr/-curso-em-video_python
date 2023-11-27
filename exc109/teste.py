'''import moeda
produ=float(input("Digite o preço: R$"))
print("A metade de {} é {}".format(produ, moeda.metade(produ)))
print("O dobro de {} é {}".format(produ, moeda.dobro(produ)))
print("Aumentando em 10%, temos R${}".format(moeda.aumentar(produ, 10)))
print("Diminuindo em 10%, temos R${}".format(moeda.diminuir(produ, 10)))'''



'''from moeda import metade, aumentar, diminuir, dobro
produ=float(input("Digite o preço: R$"))
print("A metade de {} é {}".format(produ, metade(produ)))
print("O dobro de {} é {}".format(produ, dobro(produ)))
print("Aumentando em 10%, temos R${}".format(aumentar(produ, 10)))
print("Diminuindo em 10%, temos R${}".format(diminuir(produ, 10)))'''



from exc109 import moeda
produ=float(input("Digite o preço: R$"))
print("A metade de {} é {}".format(moeda.moeda(produ), moeda.metade(produ, True)))
print("O dobro de {} é {}".format(moeda.moeda(produ), moeda.dobro(produ, True)))
print("Aumentando em 10%, temos {}".format(moeda.aumentar(produ, 10, True)))
print("Diminuindo em 10%, temos {}".format(moeda.diminuir(produ, 10, True)))

