#!/usr/bin/python

fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name


#line = fo.readline()
#print "Read Line: %s" % (line)

# Now truncate remaining file.
fo.truncate()

# Try to read file now
line = fo.readline()
print "Read Line: %s" % (line)

# Close opend file
fo.close()
