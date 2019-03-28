#!/c/Python36/python

def detail(initial, name='xxxx', age=27, hight=190, weight=80):
    print("INITIAL: %s" % initial + "\nNAME: {:8s}".format(name) + "\nAGE: {:8d}".format(age) + "\nHIGHT: %s" % hight + "\nWEIGHT: %s" % weight )

detail(initial='A', name='yyyy', age=34, weight=179, hight=30)

def sum(a,b):
    print(a+b)
    return a+b

sum(2,3)
c=sum(4,5)
print(type(c))
