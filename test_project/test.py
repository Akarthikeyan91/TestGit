#!/c/Python36/python

import library
import library.sublib.innersub
from library.sublib.innersub import *

##########
a=library.add(3,4)
print("The sum is", a)

print("The Delete is", library.dele(10,5))
print("The Multi is", library.mul(4,5))
print("The Divition is", library.div(20,4))
print("The Exponention is", library.sublib.expo(2,2))
print("The Module is", library.sublib.innersub.modu(15,2))
print("The Module is", modu(20,3))
