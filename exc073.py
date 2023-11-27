times=("Corinthians", "Palmeiras", "Santos", "Grêmio",
       "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
       "Atlético", "Botafogo", "Atlético-PR", "Bahia",
       "São Paulo", "Fluminense", "Sport-Recife",
       "EC Vitória", "Coritiba", "Avaí", "Ponte-Preta",
       "Atlético-GO")
print("-="*15)
print("Lista de times: {}".format(times))
print("-="*15)
print("Os 5 primeiros times são: {}".format(times[0:5]))
print("-="*15)
print("Os 4 últimos são: {}".format(times[-4:]))
print("-="*15)
print("Os times em ordem alfabetica são: {}".format(sorted(times)))
print("-="*15)
print("A Chapecoense está na {}ª posição".format(times.index("Chapecoense")+1))



