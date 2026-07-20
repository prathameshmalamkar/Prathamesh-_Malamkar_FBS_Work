#### Q9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) ?

#lets take input of 5 subject marks:

sub1=int(input("enter marks of subject 1:"))

sub2=int(input("enter marks of subject 2:"))

sub3=int(input("enter marks of subject 3:"))

sub4=int(input("enter marks of subject 4:"))

sub5=int(input("enter marks of subject 5:"))

total_marks=500

# lets calculate percentage

if sub1<=100 and sub2<=100 and sub3<=100 and sub4<=100 and sub5<=100:
    obt_total_marks=sub1+sub2+sub3+sub4+sub5
    percentage=obt_total_marks/total_marks*100
    
    if percentage >=90:
        print("Grade : Distinction!")
        
    elif percentage >=75:
        print("Grade : first class!")
        
    elif percentage >60:
    
        print("Grade : second class!")
        
    elif percentage >=35:
        print("Grade : third class!")
    else:
        print("Grade: fail!")          
