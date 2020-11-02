names = ["A", "B", "C","D","E","F"]

peopleNo = len(names) - 6

if peopleNo > 5:
    print("There is being mob int the room")
elif peopleNo >= 3 and peopleNo <= 5 :
    print("Room is crowded")
elif peopleNo == 1 or peopleNo == 2:
    print("Room is not crowded")
elif peopleNo == 0:
    print("Room is empty")
