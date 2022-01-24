#Ques 1: Find average of three numbers by taking inputs from user
  
#Define variables to take inputs
a = int(input("What is the first number?"))
b = int(input("What is the second number?"))
c = int(input("What is the third number?"))
  
#Define variable to print average
average = (a+b+c)/3

#Print the formula for finding average
print ("Formula to calculate average = sum of the numbers/3")

#Print result
print ("Average of the three numbers is " + str(average))

#Output: 
#What is the first number?3
#What is the second number?3
#What is the third number?3
#Formula to calculate average = sum of the numbers/3
#Average of the three numbers is 3.0


#Ques 2: Write a python program to compute a person's income tax.

#Define variables to take input
gross_income = float(input("Put your gross income($): "))
dependents = int(input("Put number of dependents: "))

#Define standard decution
standard_deduction = 10000

#Define formula for taxable income 
taxable_income = gross_income - standard_deduction - (3000*dependents)

#Define formula for income tax
income_tax = taxable_income*(20/100)

#Print result
print("Your income tax is " + str(income_tax))

#Output:
#Put your gross income($): 70000.92
#Put number of dependents: 2
#Your income tax is 10800.184000000001


# Question 3 : To store different data type values into a list.

Name = input("Enter the name of the Student: ")
SID = int(input("Enter the Student Id: "))
Gender = input("Enter the gender of the Student(F, M, U): ")
Course_name = input("Enter the Student's course name: ")
CGPA = float(input("Enter the Student's CGPA: "))

Student_list = ['Name', 'SID', 'Gender', 'Course name', 'CGPA']
print(Student_list)

Student_info = [Name, SID, Gender, Course_name, CGPA]
print("\n The list of the Student information:\n ", Student_info)

# Question 4 : Make a list to enter marks of 5 students into a list and display them in a sorted manner.

student1_marks = int(input("Enter the marks of the Student 1: "))
student2_marks = int(input("Enter the marks of the Student 2: "))
student3_marks = int(input("Enter the marks of the Student 3: "))
student4_marks = int(input("Enter the marks of the Student 4: "))
student5_marks = int(input("Enter the marks of the Student 5: "))

student_markslist = [student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]
print("\n List of the Student Marks:\n ", student_markslist)

# Sorted List
print("\n Sorted Student List (increasing order): ")
student_markslist.sort()
print(student_markslist)

# Question 5:
# (a) Print a specified list after removing 4th element i.e. Black.
# (b) Remove Black and Pink from the list and replace it with Purple.

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Print (a) part
print('\n (a)')
print(color_list)
# Remove 4th element that is Black
color_list.remove('Black')
print("\n List after removing Black Color:\n ", color_list)

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Print (b) part
print('\n (b)')
print(color_list)
# Replace Black and Pink with Purple
color_list[3:5] = ['Purple']
print("\n List after replacing Black and Pink with Purple Color:\n ", color_list)
