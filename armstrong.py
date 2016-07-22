n=input("enter a number")
s=0
a=n
while(n>0):
	n1=n%10
	s=s+(n1*n1*n1)
	n=n/10
if(s==a): 
	print "armstrong number"
else:
	print "not armstrong"
