num=(int(input("Digite um número:")),
     int(input("Digite outro número:")),
     int(input("Digite mais um número:")),
     int(input("Digite o último número:")))
print("Você digitou os valores: {}".format(num))
print("O valor 9 apareceu {} vezes".format(num.count(9)))
if 3 in num:
     print("O valor 3 apareceu na {}ª posição".format(num.index(3)+1))
else:
     print("O valor 3 não foi digitado em nehuma posição")
print("Os valores pares digitados foi:", end=" ")
for n in num:
     if n % 2 == 0:
          print("{}".format(n), end=" ")
     '''else:
          print("Nenhum número par foi digitado")
          break'''