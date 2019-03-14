#!/usr/bin/python


# Adding odd numbers without using recursion 

add_initial = 0
for i in (range(100)):
    add_value = i + add_initial
    if add_value % 2 == 1:
         add_initial = add_value
print(add_initial)
~                         
