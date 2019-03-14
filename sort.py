#!/usr/bin/python

# Removing and sorting two different list's
'''
l1 = [23,45,-9,8,9,0,4,5,78,-56,-98]
l2 = [0,3,4,-98,34,567,78,-23,45,9,0,1]
l3_duplicate = []
l4_sort = []
l2.extend(l1)
for i in l2:
   if i not in l3_duplicate:
       l3_duplicate.append(i)
print(l3_duplicate)
while l3_duplicate:
    low = l3_duplicate[0]
    for i in l3_duplicate:
        if i < low:
            low = i  
    l4_sort.append(low)
    l3_duplicate.remove(low)
print(l4_sort)
'''

#Removing the duplicate elements from a list by using list comphrehension & normal method

l1 = [2,3,4,5,6,67,89]
l2 = [67,45,3,3,4,5,2]
l3 = []
l1.extend(l2)
for i in l1:
    if i not in l3:
        l3.append(i)
print (l3)
