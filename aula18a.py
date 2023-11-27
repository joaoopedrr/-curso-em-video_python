'''teste=[]
teste.append("Gustavo")
teste.append(40)
galera=[]
galera.append(teste)
teste[0]= "Maria"
teste[1]= 22
galera.append(teste)
print(galera)


teste=[]
teste.append("Gustavo")
teste.append(40)
galera=[]
galera.append(teste[:])
teste[0]= "Maria"
teste[1]= 22
galera.append(teste[:])
print(galera)'''



'''galera=[["João", 33], ["Ana", 17], ["Joaquim", 20], ["Lourdes", 40]]
print(galera[2])

galera=[["João", 33], ["Ana", 17], ["Joaquim", 20], ["Lourdes", 40]]
print(galera[2][1])'''



'''galera=[["João", 33], ["Ana", 17], ["Joaquim", 20], ["Lourdes", 40]]
for p in galera:
    print(p)

galera=[["João", 33], ["Ana", 17], ["Joaquim", 20], ["Lourdes", 40]]
for p in galera:
    print(p[0])'''



'''galera=[["João", 33], ["Ana", 17], ["Joaquim", 20], ["Lourdes", 40]]
for p in galera:
    print("{} tem {} anos de idade".format(p[0], p[1]))'''

galera=[]
dado=[]
totmaior=0
totmenor=0
for c in range(0, 3):
    dado.append(str(input("Nome:")))
    dado.append(int(input("Idade:")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print("{} é maior de idade".format(p[0]))
        totmaior=totmaior+1
    else:
        print("{} é menor de idade".format(p[0]))
        totmenor=totmenor+1
print("Temos {} maiores de idade e {} menores de idade".format(totmaior, totmenor))


