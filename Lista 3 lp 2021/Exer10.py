quant = 1
valortot = 0
id = int(input("Entre com o codigo do produto: "))
while id > 0:
    if id == 100:
        valortot = valortot + 4.50
        print("Misto quente")
        id = int(input("Entre com o codigo do produto: "))
    if id == 101:
        valortot = valortot + 5.00
        print("Refrigerante")
        id = int(input("Entre com o codigo do produto: "))
    if id == 102:
        valortot = valortot + 2.00
        print("Pao de queijo")
        id = int(input("Entre com o codigo do produto: "))
    if id == 103:
        valortot = valortot + 6.00
        print("Suco")
        id = int(input("Entre com o codigo do produto: "))        
print("Total a pagar:",valortot)        