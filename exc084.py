temp=[]
principal=[]
cont=0
maior=0
menor=0
while True:
    temp.append(str(input("Nome:")))
    temp.append(float(input("Peso:")))
    if len(principal) == 0:
        maior=temp[1]
        menor=temp[1]
    else:
        if temp[1] > maior:
            maior=temp[1]
        if temp[1] < menor:
            menor=temp[1]
    principal.append(temp[:])
    temp.clear()
    resp=str(input("Quer continuar: [S/N]"))
    if resp in "Nn":
        break
    cont = cont + 1
print("-="*30)
print("Os dados foram {}".format(principal))
#print("Ao todo, você cadastrou {} pessoas".format(len(principal)))
print("Ao todo, você cadastrou {} pessoas".format(cont+1))
print("O maior peso foi de {}Kg. Peso de ".format(maior), end=" ")
for p in principal:
    if p[1] == maior:
        print("[{}]".format(p[0]), end=" ")
print()
print("O menor peso foi de {}Kg. Peso de ".format(menor), end=" ")
for p in principal:
    if p[1] == menor:
        print("[{}]".format(p[0]), end=" ")
print()

