#!/c/Python36/python

List = [(0,1),(1,2),(2,-1)]
order=[]
[order.append(i[1]) for i in List]
print("The 2nd lowest value from all the 2nd indices of tuple is: ",sorted(order)[1])

x = [(0,1),(1,2),(2,-1)]
new_list=[]
for i in x:
    new_list.append(i[1])
    new_list.sort()
print (new_list[1])

####
a=([i[1] for i in x])
print(sorted(a)[1])

print(sorted([i[1] for i in x])[1])    #### simpletest 
####

List = [(0,1),(1,2),(2,-1),(5,0)]
l=dict(List)
print(l)
l1=[]
for j in sorted(l.values()):
      l1.append(j)
print(l1[1])

####

List = [(0,1),(1,2),(2,-1),(5,0)]
l=[]
for i in range(len(List)):
    for j in List[i]:
        l.append(j)
#print(l)
l1=[]
for i in range(1,len(l),2):
    l1.append(l[i])
#print(l1)
for i in range(0,len(l1)):
    for j in range(0,len(l1)-1):
        if l1[j]>l1[j+1]:
          l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1[1])

