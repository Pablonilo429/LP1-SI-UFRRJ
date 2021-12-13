pesid = 0 
sex = (input("Selecione seu sexo(F para feminino e M para masculino): "))
altura = float(input("Entre com a sua altura: "))
if sex == 'F':
    pesid = (62.1*altura)-44.7
if sex == 'M':
    pesid = (72.7*altura)-58.0
print("O peso ideal para sua altura e de:", pesid, "KG")        