for _ in range(3):
    y = list(map(int, input().split()))
    if y.count(0) == 1:
        print("A")
    elif y.count(0) == 2:
        print("B")
    elif y.count(0) == 3:
        print("C")
    elif y.count(0) == 4:
        print("D")
    else:
        print("E")