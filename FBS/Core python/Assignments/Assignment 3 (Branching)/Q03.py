#### Q3.Write a program to input angles of a triangle and check whether triangle is valid or not ?

## Check the triangle is valid or not

# input the three angles of a triangle
angle1=int(input("Enter your first number."))
angle2=int(input("Enter your second number."))
angle3=int(input("Enter your third number."))

# calculate the addition in three numbers
sum=angle1+angle2+angle3
if sum==180:
    print("Triangle is valid.")
else:
    print("Triagle is invalid.")
