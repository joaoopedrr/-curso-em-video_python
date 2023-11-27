nota1=float(input("Qual foi a primeira nota:"))
nota2=float(input("Qual foi a segunda nota:"))
media= (nota1+nota2)/2
print("Tirando {} e {}, sua média foi de {}".format(nota1, nota2, media))
if media<5:
    print("O aluno está reprovado")
elif media>=5 and media<7:
    print("O aluno está em recuperação")
elif media>=7:
    print("O aluno está aprovado")


