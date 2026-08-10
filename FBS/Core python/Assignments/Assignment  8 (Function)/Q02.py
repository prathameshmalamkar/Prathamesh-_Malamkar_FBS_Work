### Q2. Write a program to calculate area of circle

## calculate the area of circle
def area_circle(radius):
    area = 3.14 *( radius * radius)
    return area

## input as a user
l = int(input("Enter your radius"))

## function call
result = area_circle(l)

## output
print(result)
