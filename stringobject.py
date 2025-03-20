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

#title()
print("\nTitle function is used to return capitalised version of each word in the input string.")
stitle=input("Please type a string with few words in small case: \n")
stitle=stitle.title()
print(stitle)

#count()
print("\nCount function is used to return the number of occurrences of the sub string in the string.")
scount1=input("Please type a string: ")
scount2=input("Enter the string for which you want the no. of occurrences")
scount=scount1.count(scount2)
print(scount)

#Startswith()
print("\nStartswith function returns a boolean value by checking if the string starts with the given substring.")
startswith1=input("Please type a string: ")
startswith2=input("Enter the substring to check if the earlier entered string starts with it or not " )
startswith=startswith1.startswith(startswith2)
print(startswith)

#Endswith()
print("\nEndswith function returns a boolean value by checking if the string ends with the given substring.\n It takes 3 parameters, suffix(can be multiple, start and end positions which are optional.")
sendswith1=input("Please type a string: ")
sendswith2=input("Enter the substring to check if the earlier entered string ends with it or not " )
sendswith=sendswith1.endswith(sendswith2)
print(sendswith)

#Index()
print("\nIndex function returns the index value of the specified value from the given substring.")
sindex1=input("Please type a string: ")
sindex2=input("Enter the value for which you want to retrieve the index: " )
sindex=sindex1.index()
print(sindex)

#Upper()
print("\nUpper function returns the string in upper case.")
supper1=input("Please type a string in uppercase or lower case or mixed case: ")
supper=supper1.upper()
print(supper)

#Lower()
print("\nLower function returns the string in lower case.")
slower1=input("Please type a string in uppercase or lower case or mixed case: ")
slower=slower1.lower()
print(slower)

#Swapcase
print("\nSwapcase function returns the string by swapping the case of the letters from Upper to Lower, vice-versa.")
sswapcase1=input("Please type a string in uppercase or lower case or mixed case(preferably): ")
sswapcase=sswapcase1.swapcase()
print(sswapcase)

#IsUpper()
print("\nIsUpper function returns boolean value True if the give string in upper case otherwise returns False.")
sisupper1=input("Please type a string in uppercase or lower case or mixed case: ")
sisupper=sisupper1.isupper()
print(sisupper)

#IsLower()
print("\nIsLower function returns boolean value True if the give string in lower case otherwise returns False.")
sislower1=input("Please type a string in uppercase or lower case or mixed case: ")
sislower=sislower1.islower()
print(sislower)

#IsAplpha
print("\nIsAlpha function returns boolean value True if the give string contains only alphabets otherwise returns False.")
sisalpha1=input("Please type a string in uppercase or lower case or mixed case: ")
sisalpha=sisalpha1.isalpha()
print(sisalpha)

#IsDigit
print("\nIsDigit function returns boolean value True if the give string contains only digits otherwise returns False.")
sisdigit1=input("Please type a string of numbers or alphabets or alphanumerics: ")
sisdigit=sisdigit1.isdigit()
print(sisdigit)

#IsAlNum
print("\nIsAlNum function returns boolean value True if the give string both alphabets and numbers otherwise returns False.")
sisalnum1=input("Please type a string of numbers or alphabets or alphanumerics: ")
sisalnum=sisalnum1.isalnum()
print(sisalnum)

#IsSpace
print("\nIsSpace function returns boolean value True if the give string contains only spaces otherwise returns False.")
sisspace1=input("Please type a string of numbers or alphabets or alphanumerics: ")
sisspace=sisspace1.isspace()
print(sisspace)

#Split
print("\nSplit function returns splitted values/words based on the specified delimeter. Default delimeter is space.")
ssplit1=input("Please type a string with spaces or delimeter of your choice: ")
ssplit2=input("Enter the delimeter: ")
ssplit=ssplit1.split(ssplit2)
print(ssplit)

#Join
print("\nJoin function returns splitted values/words based on the specified delimeter. Default delimeter is space.")
ssplit1=input("Please type a string with spaces or delimeter of your choice: ")
ssplit2=input("Enter the delimeter: ")
ssplit=ssplit1.split(ssplit2)
print(ssplit)
