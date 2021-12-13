sele = []
h = 0
num = int(input("Entre com um valor: "))
while num >=0:
    print("Entre com um valor:")
    sele.insert(h, num)
    h= h + 1
    num = int(input())

for i in range(len(sele)):
    val_min = i
    for j in range(i+1, len(sele)):
        if sele[val_min] > sele[j]:
            val_min = j
                      
    sele[i], sele[val_min] = sele[val_min], sele[i]
taman1 = len(sele)
print ("Maior numero:",sele[taman1-1])
print ("Menor numero:", sele[0])