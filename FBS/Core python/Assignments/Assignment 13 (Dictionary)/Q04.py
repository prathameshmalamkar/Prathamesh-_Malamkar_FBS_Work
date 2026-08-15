### Q4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def create_dict(n):
    dict = {}
    
    for x in range (1, n + 1):
        dict[x] = x * x
    return dict

a = int(input("Enter a numbers :"))

res = create_dict(a)

print(res)
    