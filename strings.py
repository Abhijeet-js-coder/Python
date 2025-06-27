#Learning about strings
course="Python's Course for Beginners"
print(course)

#For Multiline we use ''' ''' Quotes . Example : When writing an Email
multiline='''
Hi John,
How's your day going ?
This is an sample email
Thank You for your time
Regards, Technical Team
'''
print(multiline)

#Searching the indexing
index="Hello, Guys I'm improving day by day"
print(index[0]) #prints H

#Negative indexing
negative_indexing="Python is an easy language to understand"
print(negative_indexing[-1]) #prints d
#print(negative_indexing[]) displays an error because it needs to be filled

# Making copy of an string 
actual="Python is used for web development"
copied=actual[:]
print(copied) #Prints the whole string of actual variable

#Guessing the output 
name='Jennifer'
print(name[1:-1])  #prints ennife