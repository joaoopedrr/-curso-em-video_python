'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print(pessoas)

pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print(pessoas["Nome"])


pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print("O {} tem {} anos".format(pessoas['Nome'], pessoas['Idade']))'''



'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print(pessoas.values())


pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print(pessoas.keys())


pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
print(pessoas.items())'''




'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
for k in pessoas.keys():
    print(k)


pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
for k in pessoas.values():
    print(k)


pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
for k, v in pessoas.items():
    print("{} = {}".format(k, v))'''



'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
del pessoas["Sexo"]
for k, v in pessoas.items():
    print("{} = {}".format(k, v))'''


'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
pessoas["Nome"] = "Leandro"
for k, v in pessoas.items():
    print("{} = {}".format(k, v))'''


'''pessoas={"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
pessoas["Nome"] = "Leandro"
pessoas["Peso"] = 98.5
for k, v in pessoas.items():
    print("{} = {}".format(k, v))'''

'''
brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)


brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)


brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])


brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1])



brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]["uf"])

brasil=[]
estado1={"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2={"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]["sigla"])'''


estado={}
brasil=[]
for c in range(0, 3):
    estado["uf"]=str(input("Unidade federativa:"))
    estado["sigla"]=str(input("Sigla do estado:"))
    brasil.append(estado.copy())
print(brasil)


estado={}
brasil=[]
for c in range(0, 3):
    estado["uf"]=str(input("Unidade federativa:"))
    estado["sigla"]=str(input("Sigla do estado:"))
    brasil.append(estado.copy())
for e in brasil:
    print(e)


estado={}
brasil=[]
for c in range(0, 3):
    estado["uf"]=str(input("Unidade federativa:"))
    estado["sigla"]=str(input("Sigla do estado:"))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print("O campo {} tem valor {}".format(k, v))



estado={}
brasil=[]
for c in range(0, 3):
    estado["uf"]=str(input("Unidade federativa:"))
    estado["sigla"]=str(input("Sigla do estado:"))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()





