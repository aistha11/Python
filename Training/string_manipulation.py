
# a = [1, 6, 7, 2, 8, 3]

# print(a[-1:-4:-1])

# text = "ThIs is a sample text"
# print(text.upper())
# print(text.lower())
# print("text".capitalize())
# print(text.title())
# print(text.swapcase())
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# print(text.replace("is",""))

"""
WAP to achieve:
Input = "   rAmesh kuMar TiWari  "
Output = first name -> Ramesh, last name -> Tiwari

Input = "   ram thapa  "
Output = first name -> Ram, last name -> Thapa
"""

inp = "   rAmesh kuMar TiWari  "
arr = inp.strip().title().split(" ")
print("First Name: ", arr[0])
print("Last Name: ", arr[-1])
# ['rAmesh', 'kuMar', 'TiWari']