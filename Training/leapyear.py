year = 100

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")


if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print("leap year")
else:
    print("not")
