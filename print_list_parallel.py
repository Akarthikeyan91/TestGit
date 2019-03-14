#!/usr/bin/python

l1=[1,2,3]
l2=[4,5,6,7,8]
for i in range(len(l1)):
    print(l1[i],end=" ")
    print(l2[i],end="\n")

def list_par(l1,l2):
    if len(l1)<len(l2):
        for i in range(len(l1)):
                print(l1[i],l2[i])

    else:
        for i in range(len(l2)):
                print(l1[i],l2[i])
print("enter elements for list1")
l1=[int(x) for x in input().split()]
print("enter elements for lis2")
l2=[int(x) for x in input().split()]
list_par(l1,l2)

a = [1,2,3,5,6,7,8,9,10]
b = [4,5,6,7,8]
for i in range(min(len(a),len(b))):
    print (a[i],b[i])
