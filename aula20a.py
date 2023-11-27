'''print("-"*30)
print("Fabrício")
print("-"*30)
print("-"*30)
print("Evanilson")
print("-"*30)
print("-"*30)
print("Givaldo")
print("-"*30)'''

'''def lin():
    print("-"*30)


lin()
print("Fabrício")
lin()
lin()
print("Evanilson")
lin()
lin()
print("Givaldo")
lin()'''



'''def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


titulo("Fabrício")'''


'''def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


titulo("Fabrício")
titulo("Python é legal!")
titulo("Vamos brincar!")'''


'''def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


titulo("Fabrício")
titulo("Evanilson")
titulo("Givaldo")'''



'''a=4
b=5
s=a+b
print(s)

a=8
b=9
s=a+b
print(s)

a=2
b=1
s=a+b
print(s)'''

'''def soma(a, b):
    s=a+b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)'''


'''def soma(a, b):
    s=a+b
    print(s)


soma(a=4, b=5)
soma(b=8, a=9)'''


'''def soma(a, b):
    print("A = {} e B = {}".format(a, b))
    s=a+b
    print("A soma de A + B = {}".format(s))


soma(4, 5)


def soma(a, b):
    print("A = {} e B = {}".format(a, b))
    s=a+b
    print("A soma de A + B = {}".format(s))


soma(b=4, a=5)'''




'''def contador(*num):
    print(num)


contador(2 , 1, 7)
contador(20, 5, 10)
contador(6, 7, 9, 23)'''



'''def contador(*num):
    for valor in num:
        print(valor)


contador(2 , 1, 7)
contador(20, 5, 10)
contador(6, 7, 9, 23)'''



'''def contador(*num):
    for valor in num:
        print("{}  ".format(valor), end="")
    print("FIM!")


contador(2 , 1, 7)
contador(20, 5, 10)
contador(6, 7, 9, 23)


def contador(*num):
    tam = len(num)
    print("Recebi os valores {} e são ao todo {} números".format(num, tam))


contador(2 , 1, 7)
contador(20, 5, 10)
contador(6, 7, 9, 23)'''



'''def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos]= lst[pos] * 2
        pos=pos+1


valores=[7, 8, 6, 3, 26, 76]
dobra(valores)
print(valores)'''




def soma(*valores):
    s=0
    for num in valores:
        s=s+num
    print("Somando os valores {} temos {}".format(valores, s))


soma(5, 2)
soma(3, 5, 7)










