'''print("Escolha um número, se quiser parar digite [999]")
num=int(input("Qual número:"))'''


'''num=0
soma=0
cont=0
while num != 999:
    num=int(input("Digite um número [999 para parar]:"))
    soma=soma+num
    cont=cont+1
print("Voçê digitou {} números e a soma entre eles foi {}".format(cont -1, soma -999))'''

num=0
soma=0
cont=0
num=int(input("Digite um número [999 para parar]:"))
while num != 999:
    soma=soma+num
    cont=cont+1
    num = int(input("Digite um número [999 para parar]:"))
print("Voçê digitou {} números e a soma entre eles foi {}".format(cont, soma))