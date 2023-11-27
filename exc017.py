'''catoposto=float(input("Qual é o comprimento do cateto oposto:"))
catajacente=float(input("Qual é o comprimento do cateto adjacente:"))
hip=(catoposto**2 + catajacente**2)**(1/2)
print("A hipetenusa vai medir {}".format(hip))'''





import math
catoposto=float(input("Qual é o comprimento do cateto oposto:"))
catajacente=float(input("Qual é o comprimento do cateto adjacente:"))
hip=math.hypot(catoposto,catajacente)
print("A hipetenusa vai medir {}".format(hip))