'''num=[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop(1)
num.remove(2)
print(num)
print("Essa lista tem {} elementos".format(len(num)))'''



'''valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print("{}...".format(v), end=" ")'''




'''valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print("Na posição {} encontrei o valor {}".format(c, v))
print("Cheguei ao final da lista!")'''




'''valores=[]
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print("Na posição {} encontrei o valor {}".format(c, v))
print("Cheguei ao final da lista!")'''



a=[2, 3, 4 ,7]
b=a
b[2]=8
print("Lista A: {}".format(a))
print("Lista B: {}".format(b))


a=[2, 3, 4 ,7]
b=a
b[2]=8
print("Lista A: {}".format(a))
print("Lista B: {}".format(b))

