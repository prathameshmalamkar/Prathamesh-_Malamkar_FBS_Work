### Q3. Write a program to accept distance in km and convert it into meters and centimeters both.

def convert(km) :
    meter =(km * 1000)
    centimeter = (km * 100000)
    
    print("Meter =", meter)
    print("Centimeter =", centimeter)
    
km = int(input("Enter distance in km :"))

convert(km)