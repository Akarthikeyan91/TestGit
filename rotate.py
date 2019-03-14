#!/usr/bin/python

list1=[1,2,3,4,5,6]
n=2

##### Right rotate ####
r1=list1[len(list1)-n:]
r2=list1[:len(list1)-n]

r1.extend(r2)
print(r1)

##### left rotate ####
l1=list1[n:]
l2=list1[:n]

l1.extend(l2)
print(l1)


l1=[1,2,3]
l2=[4,5,6,7,8]
for i in range(len(l1)):
    print(l1[i],end=" ")
    print(l2[i],end="\n")

'''
squares = {}

for n in range(10):
    squares[n] = n ** 2

# print out the contents of the squares dict
print(squares)
for key, value in squares.items():
    print key, value
'''
