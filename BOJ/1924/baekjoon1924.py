x, y = map(int, input().split())

month_big = [1, 3, 5, 7, 8, 10, 12]
month_small = [4, 6, 9, 11]
month_leap = [2]

day = 0

for i in range(1, x):
    if i in month_big:
        day += 31
    elif i in month_small:
        day += 30
    elif i in month_leap:
        day += 28

day += y

if day % 7 == 0:
    print("SUN")
elif day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")