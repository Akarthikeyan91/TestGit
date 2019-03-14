#!/usr/bin/python

# Verifying and removing vowels from the string

import re
Char = ("element of individuality")
char_final = []
char_vowels = []
regex = re.compile("[aeiou]")
if isinstance (Char,str):
     for i in Char:
         if re.search(regex,i) == None:
             char_final.append(i)
         else:
             char_vowels.append(i)
if len(char_final) + len(char_vowels) == len(Char):
     print ("elements are seggregated")
else:
     print ("elements are missing")
print (char_final)
print (char_vowels)
