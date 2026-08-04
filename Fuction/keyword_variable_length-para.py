#1. To pass multiple value with meaning to function
#2. Mention 2 asterisk(**) symbol before parameter name in function definition
#3. Data stored in dictionary format
#4. Use for loop on dict.items() to access individually

def emp(**data):
    for key, val in data.items():
        print(key, ":", val)
        
emp(id = 101, name = "Pratham", age = 23, add = "Pune")