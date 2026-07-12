####  Q1. Write a program to calculate the percentage of student based on marks of any 5 subject ?

# so we gonna calculate to percentage of a student.
# based on marks of 5 subject

Total_marks=500

# now we are gonna get input user of all obtained marks in each subject. and each subject marks has to be smaller than or equal to 100

sub1=int(input("enter your subject 1 marks:"))
sub2=int(input("enter your subject 2 marks:"))
sub3=int(input("enter your subject 3 marks:"))
sub4=int(input("enter your subject 4 marks:"))
sub5=int(input("enter your subject 5 marks:"))

# lets all 5 subject marks to get it sums

Total_obtained_marks=sub1+sub2+sub3+sub4+sub5

# formula of percentage is obtained marks/total marks *100

Percentage=Total_obtained_marks/Total_marks*100

#Display result

print(Percentage)
