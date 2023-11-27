num=[]
pares=[]
impares=[]
while True:
    num.append(int(input("Digite um número:")))
    resp=str(input("Você quer continuar? [S/N]")).upper()
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("-="*30)
num.sort()
print("A lista completa é {}".format(num))
print("A lista de pares é {}".format(pares))
print("A lista de impares é {}".format(impares))
