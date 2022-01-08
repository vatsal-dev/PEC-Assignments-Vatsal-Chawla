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
