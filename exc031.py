distancia=float(input("Qual é a distância em Km da sua viagem:"))
if distancia<=200:
    preço=distancia*0.50
else:
    preço=distancia*0.45
print("Você terá que pagar R${} pela viagem".format(preço))
