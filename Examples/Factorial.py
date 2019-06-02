def factorial(n):
  if(n==1):
    return 1
  else:
    return n*factorial(n-1)
  
n=int(input("Enter a number "))
if(n<0):
  print("Factorial cannot be calculated for negative number.")
elif(n==0):
  print("Factorial is 1")
else:
  f=factorial(n)
print("Factorial of",n,"is",f)