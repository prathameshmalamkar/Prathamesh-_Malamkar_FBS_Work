n = int(input("Enter number of elements :"))

li = []

for i in range (1, n+1):
    num = int(input("Enter number {i} :"))
    
    li += [num]
    
print (li)