#Ans1
print("Ans1")
#Ask user for input
statement = str(input("Enter the statement here:"))

#count occurences of words if whitespace character is detected
if " " in statement: 
    #split at spaces and store words in a list
    statement_list = statement.split()
    statement_dict = {}
    #store list items as a dictionary with key = word, occurence = value
    for word in statement_list:
        if word in statement_dict:
            statement_dict[word] += 1
        else:
            statement_dict[word] = 1
    #pretty print dictionary for better readability
    import pprint
    pprint.pprint(statement_dict)
#if no whitespace detected: find occurences of letters
else: 
    statement_dict = {}
    #store each character in dictionary with key = character, value = occurence
    for chr in statement:
        if chr in statement_dict:
            statement_dict[chr] += 1
        else:
            statement_dict[chr] = 1
    #pretty print the dictionary
    import pprint
    pprint.pprint(statement_dict)

#----------------------------------------------------

#Ans2
print("Ans 2")

#Take input of date from user
day=int(input('Please enter Day- '))
month=int(input('Please enter Month- '))
year=int(input('Please enter Year- '))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True

#After checking condition, following code executes (if-else)
if condition:
    #checking and changing for new year
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1
                    
    #covering all the remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    #printing the calculations
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")
else:
    #gives a warning and ends the program
    print("Invalid date")


#----------------------------------------------------

#Ans3
print("Ans 3")

#Ask user for input of integers
numberInput = str(input("Enter the list of numbers (separated with space): \n "))

#Converting string input to list
numberList = numberInput.split()

#Converting each item of list to integer (string till now)
for i in range(len(numberList)):
    numberList[i] = int(numberList[i])

#Forming tuples and storing it in a list
squarelist = [(numberList[i], numberList[i]**2) for i in range(len(numberList))]

print(squarelist)


#----------------------------------------------------
#Ans4
print("Ans 4")

#Ask user for input
grade_point_input = int(input("Enter Grade Point - "))

#if-else to check if input is in range
if (4 <= grade_point_input <= 10):
     grade_points = [4,5,6,7,8,9,10]
    
     ind = grade_points.index(grade_point_input)
      
     grade_letter = ["D", "C", "C+", "B", "B+", "A", "A+"]
     grade_performance = ["Poor", "Below Average", "Average", "Good", "Very Good", "Excellent", "Outstanding"]
      
     print ("Your grade is '%s' and %s Performance" % (grade_letter[ind], grade_performance[ind]))
else:
    print("Grade Point is Out of Range")


#----------------------------------------------------

#Ans5
print('Ans 5')

#Make list of alphabets
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

#if-else to print inverted pyramid
for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")

#----------------------------------------------------
#Ans 6

#Use if-else to ask if the user wants to input student details or not
student_dict = {}
while True:
    decision = input("Type Y to enter student details, otherwise type N: ")
    if decision == 'Y' or decision == 'y':
        name = str(input("Enter the name:"))
        sid = int(input("Enter the SID:"))
        student_dict[sid] = name
    elif decision == "N" or decision == 'n':
        print("Program Input Mode ended.")
        break
    continue

#Ans a)
print("Ans a. Details of students - ")
for key,value in student_dict.items():
    print(f"SID = {key}, Name = {value}")
print("")

#Ans b)
print("Ans b")
Val_sort_dict= sorted(student_dict.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

#Ans c)
print("Ans c")
Key_sort_dict= sorted(student_dict.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

#Ans d)
print("Ans D")

# Ask for user input for SID to be finded
SID_find = int(input("Please enter the student's SID whose detail you need- "))

if SID_find in student_dict.keys():
    print(f"Name of the required student is {student_dict[SID_find]}")
else:
    print("The SID is not present in the given Data")
print("")

#----------------------------------------------------




