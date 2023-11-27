def area(larg, comp):
    a=larg*comp
    print("A área de um terreno {}x{} é de {}m²".format(larg, comp, a))


print("Controle de terrenos")
print("-"*30)
l=float(input("LARGURA (m): "))
c=float(input("COMPRIMENTO (m): "))
area(l, c)


'''def total(n1, n2):
    soma=n1+n2
    media=soma/2
    print("A sua primeira nota foi {} e a segunda foi {}, tendo ficado com a média {}.".format(n1, n2, media))

print("CALCÚLO DE MÉDIA")
print("-"*30)
nota1=float(input("Qual foi a sua primeira nota: "))
nota2=float(input("Qual foi a sua segunda nota: "))
total(nota1, nota2)'''

