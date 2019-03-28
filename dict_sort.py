#!/c/Python36/python 


dictionary1={"abcd":1436,"vaa":821,"bat":6782}
print(dict(sorted(dictionary1.items(),key=lambda x:x[0])))
print(dict(sorted(dictionary1.items(),key=lambda x:x[1])))


import operator
dictionary1={"d":14,"a":23,"b":6,"c":17}
print(dict(sorted(dictionary1.items(), key=operator.itemgetter(0))))
print(dict(sorted(dictionary1.items(), key=operator.itemgetter(1))))
