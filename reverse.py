#!/c/Python36/python

###### String reverse with range ######
s = "Hello"
s1= ""
n = len(s) + 1
for i in range(-1,-n,-1):
    s1 =  s1 +  s[i]
print(s1)

s = "Hello"             ###### simplest way
print(''.join(s[i] for i in range(-1,-(len(s)+1),-1)))

print(''.join(reversed('a string')))      ###### sorted

###### String reverse with slice operation #######
s='python'
print(s[::-1])

###### String reverse with for loop ##########
def reverse(text):
    s=''
    for i in text:
        s= i + s
    return s

print(reverse('hai'))
    

###### String reverse with recursive method ##########
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]
  
s = "Geeksforgeeks"
  
print("The original string  is : ") 
print(s) 
  
print("The reversed string(using recursion) is : ") 
print(reverse(s)) 

##################################################
# Python code to reverse a string  
# using reversed() 
  
# Function to reverse a string 
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",) 
print (s) 
  
print ("The reversed string(using reversed) is : ") 
print (reverse(s))
