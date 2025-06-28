#In this file you'll be easily understand the string methods and how they are used 

#Calculating total number of characters in a string 
course='Python course for everyone ! '
print(len(course))  #prints 29 . len() is a general purpose function can be used if an user exceedes an limit while entering the data in the field/ form. 

#Converting into Uppercase
print(course.upper())
print(course) #The actual string won't be modified 

#Converting into Lowercase 
print(course.lower())

#Finding the letter in the string 
print(course.find('P')) #It prints the index of the letter 'P' i.e. 0
print(course.find('0')) #The find() function is case sensitive so there's a different between 'o' and 'O' . In this declaration, -1 will be printed because,  'O' is not available in the string 

print(course.find('everyone')) #prints 18 because the starting index of letter 'e' is 18

#Replacing anything in our string
print(course.replace('Python','Java'))

#Checking if ther's a particular letter or characters available in a string using 'in' operator ---> returns boolean value 
print("Python" in course) 
