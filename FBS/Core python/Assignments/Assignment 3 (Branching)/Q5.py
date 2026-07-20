#### Q5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle ?

## Check the type of triangle

# Input the three angles of user
angle1=int(input("Enter your first angle."))
angle2=int(input("Enter your second angle."))
angle3=int(input("Enter your third angle."))

# Check the three angle are  equal
if(angle1 == angle2 == angle3):
    print("Equilateral Triangle")
    
# Check the two angle are equal
elif(angle1 == angle2 or angle1 == angle3 or angle2 == angle3):
    print("Isosceles Triangle")
    
# If no angle are equal
else:
    print("Scalene Triangle")