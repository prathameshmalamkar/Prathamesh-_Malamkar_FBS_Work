#### Q3. Accept no. of passengers from user and per ticket cost. Then accept age of each
#### passenger and then calculate total amount to ticket to travel for all of them based on
#### following condition :
#### a. Children below 12 = 30% discount
#### b. Senior citizen (above 59) = 50% discount
#### c. Others need to pay full.

## input as a number of passengers
n_pasg = int(input("Enter number of passengers:"))

## inilization of total amount
total_amt = 0

## using of for loop in number of passengers
for i in range (1, n_pasg + 1):
    ticket_p = int(input(f"enter ticket price of passengers is {i}:"))
    age = int(input(f"enter age of passengers is {i}:"))
    
    if age < 12 :
        ticket_p = ticket_p -(ticket_p*30/100)
        print(f"\n ticket price for person {i} is {ticket_p}:")
    elif age > 59 :
        total_cost = ticket_p -(ticket_p*50/100)
        print(f"\n ticket price for person {i} is {ticket_p}:")
    else:
        print(f"\n ticket price for person {i} is {ticket_p}:")
        
## check the total amount ticket to travel for all passengers
    total_amt += ticket_p
else:
    print(f"total amount of passenger {ticket_p} is {total_amt}:")