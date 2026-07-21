#### Q7.Write a program to print all integers upto n that aren’t divisible by 2 and 3 ?

#  the  input as n
n=int(input("Enter your number:"))

# the loop for 1 to n 
for i in range(1,n+1):

# the number is not divisible by 2 and 3
    if i%2!=0 and i%3!=0:
        print(i)