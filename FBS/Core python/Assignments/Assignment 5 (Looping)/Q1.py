#### Q1. Write a program to prompt user to enter userid and password. If Id and
#### password is incorrect give him chance to re-enter the credentials. Let him try 3
#### times. After that program to terminate.

## set a id and password
id = "pratham"
password = "123"

## input a user id and password from user
id_1 = input("Enter your id:")
pass_w = input("Enter your password:")

## check if user id and password
if id == id_1 and password == pass_w:
    print("Login successfull.")
else:
    
## check for loop in three attempt
    for i in range (1,4):
        if id == id_1 and password == pass_w:
            break
        
## display result 
    else:
        print("Try again.")