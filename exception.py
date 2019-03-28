#!/c/Python36/python

import sys


######### Rasing an Error ###########
try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise ValueError("valueerror");  
    else:  
        print("the age is valid")  
except ValueError as e:  
    print("The age is not valid", e)


######  exception ########
try:
    print(4/0)
except ZeroDivisionError:
    print("Zerodivision ERROR")

try:
    print(x)
except Exception as e:
    print(e)


###### Multiple exception ########
try:
    print(4/0)
    #print(4/0)
except (NameError, ValueError, ZeroDivisionError) as e:
    print(e)

####### Printing Type of ERROR with sys module ########

try:
  print(x)
except:
  print("Variable", sys.exc_info()[0])      #### class with Type
  print("Variable", sys.exc_info()[1])      #### Value
  print("Variable", sys.exc_info()[2])      #### Traceback

####### Printing Type of ERROR with type function #######

try:
  print(x)
except Exception as e:
    print("Type of Class is", type(e).__class__)
    print("Type of Error is", type(e).__name__)
    print("Type of Arg is", type(e).args)

'''
##### not works in 3.6 ###########
try:
    the_file = open("the_parrot")
except IOError, (ErrorNumber, ErrorMessage):
    if ErrorNumber == 2: # file not found
        print "Sorry, 'the_parrot' has apparently joined the choir invisible."
    else:
        print "Congratulation! you have managed to trip a #%d error" % ErrorNumber
        print ErrorMessage


##### Exception with Argument #### not works in 3.6
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, (Argument):
      print("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");
'''

