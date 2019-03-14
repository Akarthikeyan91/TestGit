#!/usr/bin/python

# Get the next word for given string 

l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
value = input("Enter the letters:")
value_input = value.upper()
for i in value_input:
    try:
        if i in l1:
            value_index = l1.index(i)
            value_index += 1
            value_string = l1[value_index]
            print (value_string)
    except IndexError:
        print ("Given {} is out range".format(i))
