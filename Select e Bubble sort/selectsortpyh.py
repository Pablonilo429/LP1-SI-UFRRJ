
sele = [38, 65, 29, 22, 77]
for i in range(len(sele)):
    val_min = i
    for j in range(i+1, len(sele)):
        if sele[val_min] > sele[j]:
            val_min = j
                      
    sele[i], sele[val_min] = sele[val_min], sele[i]
print (sele)
