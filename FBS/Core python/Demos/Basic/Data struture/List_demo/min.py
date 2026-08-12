li = [45, 34, 81, 77, 53, 34, 26, 82]

min = li[0]

for ind in range (1, len(li)):
    if (li[ind] < min):
        min = li[ind]
        
print("Minimum element :", min)