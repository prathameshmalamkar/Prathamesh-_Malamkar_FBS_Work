### Q3. A farmer has a field which is half in circle share and rest rectangle.
###  He needs to do fencing for entire field using barbed wire 5 times. 
###  Circular section has radius 20m and rectangle length is 50 m and breadth is 40m.  
###  If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

radius = 20
length = 50
breadth = 40
rate = 35
pi = 3.14

perimeter = length + breadth + length + (pi * radius)

total_wire = perimeter * 5

total_cost = total_wire * rate

if total_cost > 0 :
    print("Total cost of fencing =", total_cost)
else:
    print("Invalid input")