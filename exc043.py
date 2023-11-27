peso=float(input("Qual é o seu peso? (Kg)"))
altura=float(input("Qual é a sua altura? (m)"))
imc= peso / (altura**2)
print("O IMC dessa pessoa é de {:.2f}".format(imc))
if imc<18.5:
    print("Você está abaixo do pesso ideal")
elif imc>=18.5 and imc <25:
    print("Você está como peso ideal")
elif imc>=25 and imc <30:
    print("Você está em sobrepeso")
elif imc>=30 and imc <40:
    print("Você está em obesidade")
else:
    print("Você está em obesidade mórbida")