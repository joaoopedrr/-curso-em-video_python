'''for c in range(1, 10):
    print(c)
print("FIM")'''


'''c=1
while c < 10:
    print(c)
    c= c + 1
print("FIM")'''


'''for c in range(1, 5):
    n=int(input("Digite um número:"))
print("FIM")'''

'''n=1
while n !=0:
    n=int(input("Digite um número:"))
print("FIM")'''


'''r="S"
while r == "S":
    n=int(input("Digite um número:"))
    r=str(input("Quer continuar? [S/N]")).upper()
print("FIM")'''



n=1
par=0
impar=0
while n != 0:
    n=int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par=par+1
        else:
            impar=impar+1
print("Você digitou {} números pares e {} números ímpares".format(par, impar))















