mylist=[]
n=int(input("Enter N"))
#read elements of list
for i in range (0,n):
  e=input()
  mylist.append(e)
#display list elements
print("Mylist: ",mylist)
#display third element
print("Third Element: ",mylist[2])
#display elements from index 3 to index n-1
print("Element from index 3 to n-1: ",mylist[3:])
#insert new element at index 3
n=int(input("Enter new element "))
mylist.insert(3,n)
#display list elements
print("Mylist: ",mylist)
#display length of list
print("Length: ",len(mylist))
#concatenate two lists
newlist=[8,7,9]
mylist+=newlist
#display list elements
print("Mylist: ",mylist)