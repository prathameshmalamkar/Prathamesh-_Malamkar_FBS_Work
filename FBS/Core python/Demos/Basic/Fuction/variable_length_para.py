#1. To pass multiple values to the function
#2. Mention asterisk(*) symbol before parameter name in function definition
#3. Values stores in tuple format
#4. Use for loop to access value individually

def add(*num):
    sum =  0
    for val in num:
        sum += val
    return sum


res = add(10, 20, 30, 40)
print("Addition:", res)