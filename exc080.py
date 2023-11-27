lista=[]
for c in range(0, 5):
    n=int(input("Digite um valor:"))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print("Adicionado na posição {} da lista".format(pos))
                break
            pos=pos+1
print("-="*30)
print("Os valores digitados em ordem foram {}".format(lista))


'''import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')'''



'''valores = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if n in valores:
        while n in valores:
            n = int(input('Valor duplicado, não vamos adicionar. Digite outro número: '))
            if not n in valores:
                break
    valores.append(n)
    print('Valor adicionado com sucesso!')
print(f'A lista formada é {sorted(valores)}')'''
