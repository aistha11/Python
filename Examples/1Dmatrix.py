x=[]
y=[]
z=[]
print("Enter order of list")
n=int(input())
m=int(input())
#read elements of first list of order n*m
print("Enter elements of first matrix: ")
for i in range(0,n):
  row=[]
  for j in range(0,m):
    e=int(input())
    row.append(e)
  x.append(row)
#read elements of second list of order n*m
print("Enter elements of second matrix: ")
for i in range(0,n):
  row=[]
  for j in range(0,m):
    e=int(input())
    row.append(e)
  y.append(row)
#add two list
for i in range(0,n):
  row=[]
  for j in range(0,m):
    e=x[i][j]+y[i][j]
    row.append(e)
  z.append(row)
#display all three lists
print("First Matrix: ",x)
print("Second Matrix: ",y)
print("Result Matrix: ",z)
#display last row of result
print("Last Row of result: ",z[n-1])