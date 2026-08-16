### Q2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

def simple_interest (p, r, t):
    si = p * r * t / 100
    
    print("Simple Interest =", si)
    
p = int(input("Enter Principal :"))
r = int(input("Enter Rate :"))
t = int(input("Enter Time :"))

simple_interest(p, r, t)