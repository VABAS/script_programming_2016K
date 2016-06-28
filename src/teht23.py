#!/usr/bin/python
#coding=UTF-8
def speeding_ticket(speed,limit):
	exceeds=speed-limit;
	if exceeds<5:
		return (0,False);
	elif exceeds<20:
		return (100,False);
	else:
		return (500,True);
print speeding_ticket(50, 50) # No fine. prints: (0, False)
print speeding_ticket(60, 50) # 100€ fine, doesn't lose license. Prints: (100, False)
print speeding_ticket(100, 50) # 500€ fine, loses license. Prints: (500, True)
