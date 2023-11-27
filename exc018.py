import math
angulo=float(input("Digite o ângulo que voce deseja:"))
seno=math.sin(math.radians(angulo))
print("O seno de {} é igual a {:.2f}".format(angulo, seno))
cosseno=math.cos(math.radians(angulo))
print("O cosseno de {} é igual a {:.2f}".format(angulo, cosseno))
tangente=math.tan(math.radians(angulo))
print("A tangente de {} é igual a {:.2f}".format(angulo, tangente))