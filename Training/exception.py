# a = "2"

# try:
#     a += 2
# except:
#     print("Exception")
# finally:
#     print(a)

# print(type(a))


"""

"""

inp = ["b", 10, 20, 15, "d", 16, 17, "a", "b"]
sums = 0
for i in range(6):
    try:
        sums += inp[i]
    except Exception as e:
        print(e)
print(sums)
