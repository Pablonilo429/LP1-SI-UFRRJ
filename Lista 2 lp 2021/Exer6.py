kmi = int(input("Digite a quilometragem inicial do odometro: "))
kmf = int(input("Digite a quilometragem final do odometro: "))
comb = int(input("Digite a quantidade de combustivel consumida: "))
valpas = int(input("Digite o total recebido dos passageiros: "))
med = (kmf-kmi)/comb
luc = valpas - (comb*2.75)
print("A media de consumo foi de:", med, "KM/L")
print("O lucro foi de:R$", luc)