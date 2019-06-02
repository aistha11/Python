x=int(input("Enter x "))  
n=int(input("Enter n "))
p=1
for i in range(0,n):
		p*=x
print('Power of ', x , ' and ' , n ,' is ', p)