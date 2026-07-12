# Program to check marriage eligibility based on gender and age

gender = input("Enter gender (m/f): ").lower()
age = int(input("Enter age: "))

if gender =='f':
    if age >= 18:
        print("Girl is eligible for marriage.")
    else:
        print("Pehle padhai kar lo.")
else:
    if age >= 21:
        print("Boy is eligible for marriage.")
    else:
        print("Pehle kama lo.")

   