### Q4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls. 

length = int(input("Enter Length of Wall: "))
height = int(input("Enter Height of Wall: "))
rate = int(input("Enter Painting Rate: "))

area = 4 * length * height

cost = area * rate

if cost > 0 :
    print("Total cost of painting =", cost)
else:
    print("Invalid input")