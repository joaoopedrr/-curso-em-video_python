total=0
totmil=0
menor=0
cont=0
barato= " "
while True:
    produto=str(input("Nome do produto:"))
    preço=float(input("Preço: R$"))
    cont=cont+1
    total=total+preço
    if preço > 1000:
        totmil=totmil+1
    if cont == 1:
        menor=preço
        barato=produto
    else:
        if preço < menor:
            menor=preço
            barato=produto
    resp=" "
    while resp not in "SN":
        resp=str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print("{:-^40}".format("Fim do programa"))
print("O total da compra foi R${:.2f}".format(total))
print("Temos {} produtos custando mais de R$1000".format(totmil))
print("O produto mais barato foi {} e custa R${:.2f}".format(barato, menor))



