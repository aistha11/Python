n= int(input("Enter a Number "))
if(n>1):
	for i in range(2,int(n/2)):
		rem=n%i
		if(rem==0):
		  break
	if(rem==0):
		print(n,"is not prime")
	else:
		print(n,"is prime")

else:
  print(n,"is prime")