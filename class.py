#!/c/Python36/python

#import pdb
#pdb.set_trace()

class Addition: 
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor 
	def __init__(self, f, s): 
		self.first = f 
		self.second = s 
	
	def display(self): 
		print("First number = " + str(self.first)) 
		print("Second number = " + str(self.second)) 
		print("Addition of two numbers = " + str(self.answer)) 

	def calculate(self): 
		self.answer = self.first + self.second 

# creating object of the class 
# this will invoke parameterized constructor 
obj = Addition(1000,2000) 

# perform Addition 
obj.calculate() 

# display result 
obj.display() 

# Class for Computer Science Student 
class CSStudent: 
	stream = 'cse'	 # Class Variable 
	def __init__(self, name, roll): 
		self.name = name 
		self.roll = roll 

# Driver program to test the functionality 
# Creating objects of CSStudent class 
a = CSStudent("Geek", 1) 
b = CSStudent("Nerd", 2) 

print("Initially")
print("a.stream =", a.stream)
print("b.stream =", b.stream)

# This thing doesn't change class(static) variable 
# Instead creates instance variable for the object 
# 'a' that shadows class member. 
a.stream = "ece"

print("\nAfter changing a.stream")
print("a.stream =", a.stream)
print("b.stream =", b.stream)

CSStudent.stream = "eee"

print("\nAfter changing a.stream")
print("a.stream =", a.stream)
print("b.stream =", b.stream)


'''
class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: a is %s, b is %s" % (self.a, self.b) 
 

# Driver Code         
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__()
print({t}) # This calls __repr__()
'''

'''
##### DATA HIDING ######
class MyClass: 
  
    # Hidden member of MyClass 
    __hiddenVariable = 10
  
# Driver code 
myObject = MyClass()      
print(myObject._MyClass__hiddenVariable) 


class Employee:  
    count = 0;  
    def __init__(self):  
        Employee.count = Employee.count+1  
    def display(self):  
        print("The number of employees",Employee.count)  
emp = Employee()  
emp2 = Employee()  
try:  
    print(emp.count)  
finally:  
    emp.display() 

class Foo:
    def bar(self):
        print "I'm doing Foo.bar()"
    x = 10

class Bar(Foo):
    def bar(self):
        print "I'm doing Bar.bar()"
        Foo.bar(self)
    y = 9

b=Bar()
b.bar()

f=Foo()
Foo.bar(f)

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


a=Employee('xxx', 5000)
a.displayCount()
a.displayEmployee()
b=Employee('yyy', 5000)
b.displayCount()
b.displayEmployee()
c=Employee('zzz', 5000)
c.displayCount()
c.displayEmployee()

print(vars(c))
print(c.__dict__)
#print(vars(Employee))

c.__dict__['salary']=6000
print(c.__dict__)
'''
