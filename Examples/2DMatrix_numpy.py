import numpy as np
x=[]
y=[]
print("Enter order of list")
n=int(input())
m=int(input())
print("Enter elements of first matrix: ")
for i in range(0,n):
  row=[]
  for j in range(0,m):
    e=int(input())
    row.append(e)
  x.append(row)
print("Enter elements of second matrix: ")
for i in range(0,n):
  row=[]
  for j in range(0,m):
    e=int(input())
    row.append(e)
  y.append(row)
a=np.array(x)
b=np.array(y)
c=a+b
print("Addition: ",c)
p=a*b
print("Element wise product: ",p)
p=np.dot(a,b)
print("Product: ",p)
t=np.trnspose(a)
print("Transpose of a: ",t)