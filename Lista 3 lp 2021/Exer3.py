vet = []
i = 0
j = 1
k = 0
quantidade = int(input("Insira a quantidade de elementos: "))
while i < quantidade:
    vet.insert(i,input())
    i = i+1
print(vet)    

while j < quantidade+1:
    print(j, "-", vet[k] )
    j = j+1
    k = k+1
print ("S - Sair ")