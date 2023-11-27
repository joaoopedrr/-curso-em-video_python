primeiro=int(input("Qual o primeiro termo:"))
razao=int(input("Qual a razão:"))
decimo=primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end="--- ")
print("ACABOU")
