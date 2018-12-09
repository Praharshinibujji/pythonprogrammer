number=int(input(""))
factorial=1
if number<0:
	print("no")
elif number == 0:
	print(1)
else:
	for i in range(1,number+1):
		factorial=factorial*i
	print(factorial)

