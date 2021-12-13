print("Entre com dois numeros inteiros:")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
while(menor != maior-1):
    menor = menor + 1
    print(menor)
        
