#This program is used to display the properties of a string object.
print(input("Here are the properties of a string object. Please press enter to proceed further..."))

#capitalize()
print("Capitalize function is used to return the capitalized version of the input string.")
scapitalize=input("Please type a string with few words in small case: \n")
scapitalize=scapitalize.capitalize()
print(scapitalize)


#center()
print("\nCenter function is used to return the centered string input string by padding with a fill character(default is space).\nThis function accepts 2 arguments, length and fill character.\nSyntax: stringobject.center(length,fill character)")
scenter=input("Please type a string with a length under 10 characters : \n")
scenter=scenter.center(20,"*")
print(scenter)

#count()
print("\nCount function is used to return the number of occurrences of the sub string in the string.")
scount1=input("Please type a string: ")
scount2=input("Enter the string for which you want the no. of occurrences")
scount=scount1.count(scount2)
print(scount)

#Endswith()
print("\nEndswith function returns a boolean value by checking if the string ends with the given substring.\n It takes 3 parameters, suffix(can be multiple, start and end positions which are optional.")
sendswith1=input("Please type a string: ")
sendswith2=input("Enter the substring to check if the earlier entered string ends with or not " )
sendswith=sendswith1.endswith(sendswith2)
print(sendswith)

#title()
print("\nTitle function is used to return capitalised version of each word in the input string.")
stitle=input("Please type a string with few words in small case: \n")
stitle=stitle.title()
print(stitle)