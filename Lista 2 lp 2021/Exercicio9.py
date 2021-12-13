import collections
i = 0
vet = []
num = int(input("Digite um numero: "))
while num > 1:
    vet.insert(i, num)
    i = i+1
    num = int(input("Digite um numero: "))   
repetido =  collections.Counter(vet)
print("O usuario digitou:", repetido)