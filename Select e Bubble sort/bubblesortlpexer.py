bubble = [54,26,45,93,22,66,44,53,67]
for contador in range(len(bubble)-1,0,-1):
        for i in range(contador):
            if bubble[i]>bubble[i+1]:
                tempo = bubble[i]
                bubble[i] = bubble[i+1]
                bubble[i+1] = tempo

print(bubble)