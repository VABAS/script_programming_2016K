#!/usr/bin/python
#coding=UTF-8
def calculator(operation,numb1,numb2):
	if operation=="add":
		return numb1+numb2;
	elif operation=="sub":
		return numb1-numb2;
	elif operation=="multiply":
		return numb1*numb2;

print calculator("add", 1, 2) # should print 3
print calculator("sub", 1, 2) # should print -1
print calculator("multiply", 1, 2) # should print 2
