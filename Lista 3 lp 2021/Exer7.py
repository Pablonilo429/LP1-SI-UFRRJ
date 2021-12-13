numbi = int(input("Insira o numero binario: "))
numdec = 0
i = 0
n = 0   
while(numbi != 0): 
        dec = numbi % 10
        numdec = numdec + dec * pow(2, i) 
        numbi = numbi//10
        i =i + 1
print(numdec)