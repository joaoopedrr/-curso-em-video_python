aluno={}
aluno["nome"]=str(input("Nome: "))
aluno["média"]=float(input("Média de {}:".format(aluno["nome"])))
if aluno ["média"] >= 7:
    aluno["situação"] = "aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "recuperação"
else:
    aluno["situação"] = "reprovado"
print("-="*30)
for k, v in aluno.items():
    print("  |{} é igual a {}".format(k, v))

