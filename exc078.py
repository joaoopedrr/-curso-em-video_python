listanum=[]
maior=0
menor=0
for c in range(0, 5):
    listanum.append(int(input("Digite um valor para a posição {}:".format(c))))
    if c == 0:
        maior=listanum[c]
        menor=listanum[c]
    else:
        if listanum[c] > maior:
            maior=listanum[c]
        if listanum[c] < menor:
            menor=listanum[c]
print("=-"*30)
print("Você digitou os valores {}".format(listanum))
print("O maior valor digitado foi {} nas posições".format(maior), end=" ")
for i, v in enumerate(listanum):
    if v == maior:
        print("{}...".format(i), end=" ")
print()
print("O menor valor digitado foi {} nas posições".format(menor), end=" ")
for i, v in enumerate(listanum):
    if v == menor:
        print("{}...".format(i),end=" ")
print()


