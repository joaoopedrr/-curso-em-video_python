matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar=0
mai2=0
scol3=0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]=int(input("Digite um valor para [{}, {}]:".format(l, c)))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
        if matriz[l][c] % 2 == 0:
            spar=spar+matriz[l][c]
    print()
print("-="*30)
print("A soma dos valores pares é {}".format(spar))
for l in range(0, 3):
    scol3=scol3+matriz[l][2]
print("A soma dos valores da terceira coluna é {}".format(scol3))
for c in range(0, 3):
    if c == 0:
        mai2=matriz[1][c]
    elif matriz[1][c] > mai2:
        mai2=matriz[1][c]
print("O maior valor da segunda linha é {}".format(mai2))
