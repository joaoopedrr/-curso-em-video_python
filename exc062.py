print("Gerador de PA")
print("=-="*10)
primeiro=int(input("Primeiro termo:"))
razao=int(input("Razão da PA:"))
termo=primeiro
count=1
total=0
mais=10
while mais != 0:
    total=total+mais
    while count <=total:
        print("{} -".format(termo), end=" ")
        termo=termo+razao
        count=count+1
    print("PAUSA")
    mais=int(input("Quantos termos você quer mostrar a mais?"))
print("Progressão finalizada com {} termos mostrados".format(total))
