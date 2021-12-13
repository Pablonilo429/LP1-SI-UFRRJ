vet = []
i = 0
print("Entre com um valor:")
num = int(input())

while num >= 0:
    print("Entre com um valor:")
    vet.insert(i, num)
    i= i + 1
    num = int(input())
    
print(sum(vet)) 
