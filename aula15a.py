'''n=0
s=0
while True:
    n=int(input("Digite um número: "))
    if n==999:
        break
    s=s+n
print("A soma vale {}".format(s))'''


'''n=0
s=0
while True:
    n=int(input("Digite um número: "))
    if n==999:
        break
    s=s+n
print("A soma vale {}".format(s))
print(f"A soma vale {s}")'''


nome="José"
idade=33
print(f"O {nome} tem {idade} anos.")
print("O {} tem {} anos.".format(nome, idade))
print("O %s tem %d anos." % (nome, idade))




