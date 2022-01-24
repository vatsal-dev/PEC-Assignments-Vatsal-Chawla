#Ques1: Run the following commands on the string 


#Define the string
sentence = "Python is a case sensitive language"

#Part a: print length of sentence
print("Part a: Length of the string = ", len(sentence))

#Part b: Reverse the order of string in one line code
print("Part b: Here's the reverse order =\n",sentence[::-1])

#Part c: using slice function store "a case sensitive" in another string
new_string = slice(10,26)
print("Here's the new variable = ", sentence[new_string])

#Part d: Replace "a case sensitive" with "a object oriented"
print("Part d: Here's the asked replacement = ", sentence.replace("a case sensitive", "a object oriented"))

#Part e: Index of "a"
print("Part e: here's the index of 'a' =", sentence.find("a"))

#Part f: Remove white spaces
print("Part f: Here's the string without white spaces:", sentence.replace(" ",""))


#Finished. 
#########################
