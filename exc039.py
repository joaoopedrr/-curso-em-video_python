print('''Qual é o seu sexo? Escolha a opção: [1] MASCULINO, [2] FEMININO ''')
opcao=int(input("Qual a sua opção:"))
if opcao==1:
    print("Bom! Vamos começar a consulta de dados")
elif opcao==2:
    print("Você é do sexo feminino, então não precisa se alistar!")
else:
    print("Opção inválida!")
nascimento = int(input("Em que ano você nasceu:"))
atual = 2023
idade = atual - nascimento
print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, atual))
if idade < 18:
    alistamento = 18 - idade
    print("Ainda faltam {} anos para o alistamento!".format(alistamento))
    ano = atual + alistamento
    print("Seu alistamento será em {}".format(ano))
elif idade > 18:
    alistamento = idade - 18
    print("Você já deveria ter se alistado há {} anos".format(alistamento))
    ano = alistamento - atual
    print("O seu alistamento foi em {}".format(ano))
else:
    print("Hora de se alistar imediatamente!")
