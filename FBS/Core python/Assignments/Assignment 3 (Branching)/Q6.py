#### Q6. Write a program to calculate profit or loss

## Input Cost price and Selling price
cp=int(input("Enter your cost price:"))
sp=int(input("Enter your selling price:"))

# check the Profit , Loss and No Profit , No Loss
if(cp > sp):
    print("It is profit.")
    
elif(sp > cp):
    print("It is loss.")
    
else:
    print("It is no profit and no loss.")
          

          