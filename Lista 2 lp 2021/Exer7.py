val = 0
quant = int(input("Insira a quantidade de macas: "))
if quant <12:
    val = 0.45
else:
    val = 0.36    
tot = quant*val
print("Total da compra:R$", tot)    