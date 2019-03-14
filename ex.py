#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', sys.argv

var1 = 1
var2 = 2

print var1
print var2

del var1,var2

var1 = 4
var2 = 5
print var1
print var2
