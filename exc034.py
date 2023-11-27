salario=float(input("Qual é o seu salário?R$"))
if salario<=1250:
    novo= salario + (salario*0.15)
else:
    novo= salario + (salario*0.10)
print("Quem ganhava R${:.2f} passou a ganhar R${:.2f}".format(salario, novo))