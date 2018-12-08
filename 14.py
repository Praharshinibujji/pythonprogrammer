number=int(input(""))
if(number<0):
	print("the number is negative")
elif(number==0):
	print("the number is zero")
else:
	number=number*(number+1)/2
print(number)
