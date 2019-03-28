#!/c/Python36/python
import re

line = "dogs Cats are smarter than Cats dogs";

matchObj = re.match( r'.*Cats', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'.*dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
   print("search --> searchObj.group() : ", searchObj.span())
else:
   print("Nothing found!!")
