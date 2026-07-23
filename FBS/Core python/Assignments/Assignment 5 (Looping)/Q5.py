#### Q1. Write a program to print prime numbers between 1 to 100 ?

## input as a user 
for i in range (1, 101):
    if (i > 1):
        for j in range (2, i // 2 + 1):
             if i % j == 0:
                break
        else:
            print(i)
    else:
        print(f'{i} is not prime number not composite!')