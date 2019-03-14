#!/usr/bin/python 

# integer numbers with minimum width
print("{1:8d}".format(12,34),"{1:8d}".format(12,34))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.6f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))


# integer numbers with minimum width

a=[1,11,111,1111,11111]
for i in a:
    print i

for i in a:
    print("{:6d}".format(i))
