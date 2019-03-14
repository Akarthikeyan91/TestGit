#!/usr/bin/python

# Using list comprehension, found square value of odd numbers.

l1=[1,2,3,4,5,6,7,8,9]
square_number=[i*i for i in l1 if i%2==1]
print(square_number)


#Validating the password

import re
pwd = input("Enter the Password")
if (len(pwd) >= 6) and (len(pwd) <= 12):
    if (re.search("[a-z]",pwd) and re.search("[A-Z]",pwd) and re.search("[0-9]",pwd) and re.search("[$#@]",pwd)) != None:
        print("Given PWD is valid")
    else:
        print("PWD is not valid")
else:
    print("PWD is not valid")
