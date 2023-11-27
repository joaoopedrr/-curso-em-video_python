def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não informar o número!\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não informar o número!\033[m")
            return 0
        else:
            return n


num1=leiaInt("Digite um número inteiro: ")
num2=leiaFloat("Digite um número real: ")
print("O número inteiro digitado foi {} e o número real foi {}".format(num1, num2))
