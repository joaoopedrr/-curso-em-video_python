casa=float(input("Qual o valor da casa: R$"))
salario=float(input("Qual é o seu salário: R$"))
anos=int(input("Quantos anos de financiamento: R$"))
prestacao= casa / (anos*12)
print("Para pagar uma casa de R${:.2f} em {} anos, o valor da prestação será de R${:.2f}".format(casa, anos, prestacao))
minimo= salario * 30/100
if prestacao <=minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NÃO PODE SER CONCEDIDO!")