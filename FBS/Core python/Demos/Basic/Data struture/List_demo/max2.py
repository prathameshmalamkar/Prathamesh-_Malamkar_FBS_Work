li = [45, 34, 81, 77, 53, 34, 26, 82]

max = li[0]
max2 = li[0]

for ind in range (1, len(li)):
    if (li[ind] > max):
        max = li[ind]
        
for ind in range (1, len(li)):
    if (li[ind] > max2) and li[ind] != max:
        max2 = li[ind]
        
print("Maximum element :", max)
print("Second maximum element :", max2)