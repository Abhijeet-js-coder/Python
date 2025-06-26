#Type conversions in PY
birth_year= input("Enter your Birth Year :")
year=2025 - int(birth_year) #if we don't add int() the python IDE will treat birth_year as a String
print('Your age currently is:',year)

# #Checking the type of an varible
print(type(birth_year)) 
print(type(year))

#Exercise : Asking an user to enter his/her weight in pounds and converting it into Kilograms 

pounds=input("Enter your weight in pounds : ")
kilograms=float(pounds)*0.45
print("Your weight in Kilograms is :",kilograms)
