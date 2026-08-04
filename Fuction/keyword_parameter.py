#1. To neglect positional parameter
#2. Assign value to parameter in function call
#3. Flow from right to left
#4. Name of parameter in function call and
#   function definition should be same

def emp(id, name, sal, dept):
    data = "ID:" + str(id) + "\n"
    data += "NAME:" + str(name) + "\n"
    data += "SALARY:" + str(sal) + "\n"
    data += "DEPARTMENT:" + str(dept) + "\n"
    return data

res = emp(name = "ABC", id = "101", dept = "IT", sal = "20000")
print(res)