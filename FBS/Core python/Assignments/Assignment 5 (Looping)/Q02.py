#### Q2. Enter number of students from user. For those many students accept marks of 5
#### subject marks from user and calculate percentage. Display all percentage and average percentage of students ?

## input as a number of student
n_student = int(input("Enter number of student:"))

## inilization of sum
sum_per = 0

## using of for loop in no of student
for i in range (1, n_student + 1):
    sub1_marks = int(input(f"sub 1 marks of student {i}:"))
    sub2_marks = int(input(f"sub 2 marks of student {i}:"))
    sub3_marks = int(input(f"sub 3 marks of student {i}:"))
    sub4_marks = int(input(f"sub 4 marks of student {i}:"))
    sub5_marks = int(input(f"sub 5 marks of student {i}:"))
    
## addition of total sub marks
    sum = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks

## formula of percentage
    perc = (sum / 500)*100
    sum_per = sum_per + perc
    
## check the all student percentage and avg perc of student
else:
    avg = sum_per / n_student
    print(f"for given {n_student} avg_per is  {avg}:")
