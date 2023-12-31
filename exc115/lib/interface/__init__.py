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

def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c=1
    for item in lista:
        print("\033[33m{}\033[m - \033[34m{}\033[m".format(c, item))
        c=c+1
    print(linha())
    opc=leiaInt("\033[32mSua opção:\033[m ")
    return opc


