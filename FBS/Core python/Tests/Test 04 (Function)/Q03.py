#### Q3. WAP to print following patterns :

n = 10

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * 17)
    else:
        print(" " * (15 - 2 * (i - 1)) + "*")