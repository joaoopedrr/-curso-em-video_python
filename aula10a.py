n1=float(input("Qual foi a primeira nota:"))
n2=float(input("Qual foi a segunda nota:"))
media=(n1+n2)/2
print("A média das notas é {}".format(media))
if media<=6:
    print("Voçê está reprovado!")
else:
    print("Voçê está aprovado!")
