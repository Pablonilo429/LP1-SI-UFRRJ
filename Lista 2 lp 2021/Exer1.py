fat = 1
num = int(input("Entre com um valor: "))
if num == 0:
    print("1")
while num > 1:
    fat = fat*num 
    num = num-1
print("Fatorial do numero:",fat)       