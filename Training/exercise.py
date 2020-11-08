"""
WAP to check if a list contains the following elements in it or not: "a", "c", "f"

eg: Input = ["a","b","c","d","e","f"] contains "a", "c" and "f"
but ["a", "z", "b"] doesn't

hint: pop operation in list used as stack
"""

# input = ["a","b","c","d","e","f"]
# stk = ["a", "c", "f"]

# for i in input:
#     try:
#         _ = stk.remove(i)
#     except ValueError:
#         print("Already Removed or Doesnot contain")
#     except Exception as e:
#         print(e)

# if len(stk) == 0:
#     print("Yes")
# else:
#     print("No")


"""
WAP to find if an series given in list is an additive sequence or not
5, 6, 11, 17, 28, .. is a additive sequence
as 5 + 6 = 11, 6 + 11 = 17, ...
"""

# inp = [5, 6, 11, 17, 28]
# flag = False


# for i in range(len(inp) - 2):
#     if inp[i] + inp[i+1] != inp[i+2]:
#         flag = True
#         break

# if flag:
#     print("Not additive")
# else:
#     print("Additive")


#optional assignment
"""WAP
    to find if a number is prime or not
"""

# num = 7

# if num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a Prime number")
#            break
#    else:
#        print(num,"is a Prime number")
# else:
#    print(num,"is not a Prime number")


"""WAP
    to find majority element in a list
    eg: ["a", "b", "b", 7, 7, 7]
    here 7 is the majority element in the list
"""

# inp = ["a", "b", "b", 7, 7, 7]



"""
WAP to calculate the value of 'a' to the power 'b'
"""
# a = 3
# b = 2
# r = 1

# print(pow(3,2))

# print(3**2)

# for i in range(0,b):
#     r = r*a

# print(r)





"""
WAP to find the sum of all the individual numbers in a nuber
eg: 245 -> 2 + 4 + 5 = 11
hint: checkout what "/" and "//" operator does
"""

# num = 245
# d1 = num//100
# d2 = (num%100)//10
# d3 = num%10
# print(d1+d2+d3)

# inp = 245
# inp = str(inp)
# sums = 0
# for i in inp:
#     sums += int(i)
# print(sums)



"""
WAP to remove repeated elements in the list but still preserve its order i.e without converting it to set
eg: input [1, 2, 3, 1, 4, 3, 9, 5, 4, 6, 1] -> output [1, 2, 3, 4, 9, 5, 6]
if elements gets repeated only use the first element as in the example above
"""

inp = [1, 2, 3, 1, 4, 3, 9, 5, 4, 6, 1]
res = []

for i in inp:
    if i not in res:
        res.append(i)

print(res)



"""
WAP to count the number of even and odd numbers from a series of numbers
I/0 -> [1, 2, 3, 4]
0/P -> {"even" : 2, "odd" : 2}
"""

# inp = [1, 2, 3, 4]

# even, odd = 0, 0

# for i in inp:
#     if (i % 2 == 0):
#         even += 1
#     else:
#         odd += 1

# print({"even": even, "odd": odd})





