n=int(input(""))
temp=n
reverse=0
while(n>0):
	dig=n%10
	reverse=reverse*10+dig
	n=n//10
if(temp==reverse):
	print "yes"
else:
	print "no"
