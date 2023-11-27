print("{:=^40}".format(" LOJAS GUANABARA "))
preco=float(input("Qual foi o valor das compras: R$"))
print('''FORMAS DE PAGAMENTO: 
[1] à vista dinheiro/cheque 
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opcao=int(input("Qual é a opção de pagamento:"))
if opcao==1:
    total=preco-(preco * 10/100)
elif opcao==2:
    total=preco-(preco * 5/100)
elif opcao==3:
    total=preco
    parcela=total/2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opcao==4:
    total=preco+(preco * 20/100)
    quantparc=int(input("Qual a quantidade de parcelas?"))
    parcela=total/quantparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(quantparc, parcela))
else:
    total=preco
    print("Opção inválida de pagamento. Tente novamente!")
print("Sua compra de R${} vai custar R${} no final".format(preco, total))
