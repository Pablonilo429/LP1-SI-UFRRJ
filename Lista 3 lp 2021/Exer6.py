numdec = int(input("Entre com um numero decimal: "))
numbi = " "
while numdec > 0:
    if(numdec%2)==0: 
        numbi = "0" + numbi
    else:
        numbi = "1" + numbi
    numdec = (numdec//2)    
print(numbi)


