## Default Parameter
#1. To make parameter optional
#2. Assigns value to parameter in function definition
#3. If we pass value to default parameter it takes passed value
   # If we don't pass value to default parameter it takes default value 
#4. Flow from right to left

def emp(id, name=None, sal=20000, dept="IT"):
    print("ID:", id)
    print("NAME:", name)
    print("SALARY:", sal)
    print("DEPARTMENT:", dept)
    
emp(101, "Pratham", 50000, "DA")
print("####################")
emp(102, "Vansh", 60000)
print("####################")
emp(103, "Jay")