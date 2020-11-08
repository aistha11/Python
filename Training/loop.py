# for i in range(10):
#     print(i)

# for i in range(0, 10, 1):
#     print(i)

# i = 0

# for i in range(10):
#     print(i)
#     if i > 3:
#         continue
#     print("Sagarmatha Colz")

# a = [1, 2, 3, 4]
# b = [2, 3, 4, 5]
# sums = []

# i = 0
# for i in range(len(a)):
#     add = a[i] + b[i]
#     sums.append(add)
# print(sums)

# for i in range(10):
#     for j in range(10):
#         print(i,j)

# a = [[1, 2], [3, 4]]
# b = [[6, 7], [8, 9]]

# row = 2
# col = 2
# result = []
# for i in range(row):
#     temp = []
#     for j in range(col):
#         temp.append(a[i][j] + b[i][j])
#     result.append(temp)
# print(result)

"""
# a = [
#     [1, 2], 
#     [3, 4]
# ]
Put all the diagonal elements in a list

"""
# a = [
#     [1, 2], 
#     [3, 4]
# ]
# row = 2
# col = 2
# result = []
# for i in range(row):
#     for j in range(col):
#         if i == j:
#             result.append(a[i][j])
# print(result)

# a = [
#     [1, 2], 
#     [3, 4]
# ]

# b = [
#     [1, 2], 
#     [3, 4]
# ]
# row, col = 2, 2

# result = []
# for i in range(row):
#     for j in range(col):
#         if i != j:
#             result.append(a[i][j] + b[i][j])
# print(result)

# a = [
#     [1, 2, 8], 
#     [3, 4, 9],
#     [5, 4, 2]
# ]

# row, col = 3, 3
# diag = []
# for i in range(row):
#     for j in range(col):
#         if i == abs(j-(row-1)):
#             diag.append(a[i][j])

# print(diag)

# for i , j in [(1, 2), (3, 4)]:
#     print(i, j)

# for i , j in zip([1, 2], [3, 4]):
#     print(i, j)

# count = 0
# for i in ["a", "b", "c", "x"]:
#     print(count)
#     count+=1
#     print(i)

# for i, el in enumerate(["a", "b", "c", "z"]):
#     print(i)
#     print(el)

"""
a = "10102"
print(a[:4])

WAP to count the number of 1010 sequences inside a long string eg: "1010 000 1010 11 101010" -> 4 
"""

# a = "1010"
# s = "1010 000 1010 11 101010"
# count = 0
# for i in range(len(s) - len(a) + 1):
#     if s[i] == a[0]:
#         if s[i+1] == a[1]:
#             if s[i+2] == a[2]:
#                 if s[i+3] == a[3]:
#                     count += 1
# print(count)

# a = "1010"
# s = "1010 000 1010 11 101010"
# ln_s = len(s)
# count = 0

# for i in range(len(s)):
#     if s[i:ln_s][:4] == a:
#         count += 1
# print(count)

# input_str = "1010000101011101010"
# count = 0
# for i in range(len(input_str) - 3):
#     if input_str[i:i+4]=="1010":
#         count += 1
# print(count)










