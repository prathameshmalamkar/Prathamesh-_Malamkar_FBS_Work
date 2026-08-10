### Q8. Print 1 to 100 in snakes and ladder pattern ?
    
start = 100
end = 90

li = []

for j in range(10):
    row = []

    for i in range(start, end, -1):
        row.append(i)
        
    if j % 2 == 1:
        row.reverse()

    li.append(row)
    
    start = end
    end = start - 10

for row in li :
    print(row)
