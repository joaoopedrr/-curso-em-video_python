'''n=int(input("Digite um número: "))
n=int(input("Digite um número"))'''

'''try:
    a=int(input("Numerador: "))
    b=int(input("Denominador: "))
    c=a/b
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print("O resultado da divisão é {}".format(c))
finally:
    print("Volte sempre! Muito obrigado!")'''



try:
    a=int(input("Numerador: "))
    b=int(input("Denominador: "))
    c=a/b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou!")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0!")
except KeyboardInterrupt:
    print("O usuário não preferiu informar os dados!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print("O resultado da divisão é {}".format(c))
finally:
    print("Volte sempre! Muito obrigado!")







