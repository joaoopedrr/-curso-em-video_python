tot18=0
sexman=0
totwoman20=0
while True:
    idade=int(input("Idade:"))
    sexo=" "
    while sexo not in "MF":
        sexo=str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18=tot18+1
    if sexo == "M":
        sexman=sexman+1
    if sexo == "F" and idade < 20:
        totwoman20=totwoman20+1
    resp= " "
    while resp not in "SN":
        resp=str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if resp== "N":
        break
print("O total de pessoas com mais de 18 anos:",format(tot18))
print("Ao todos temos {} homens cadastrados".format(sexman))
print("E temos {} mulheres com menos de 20 anos".format(totwoman20))
