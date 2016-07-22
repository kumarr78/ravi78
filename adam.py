import math
def reverse(x):
	Reverse = 0
	while(x > 0):
		Reminder = x %10
		Reverse = (Reverse *10) + Reminder
		x = x/10
	return Reverse
n=input("enter a number:")
f1=int(math.pow(n,2))
f2=int(math.pow(reverse(n),2))
if(f2 == reverse(f1)):
	print "adam number"
else:
    print "not adam number"	