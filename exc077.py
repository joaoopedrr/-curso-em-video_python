palavras=("aprender", "programar", "linguagem", "python",
          "curso", "grátis", "estudar", "praticar",
          "trabalhar", "mercado", "programador", "futuro")
for p in palavras:
    print("\nNa palavra {} temos as vogais:".format(p.upper()), end=" ")
    for letra in p:
        if letra.lower() in "aáãâeéêiíîoóõôuúû":
            print(letra, end=" ")
