n = int(input())
result = []

for i in range(n):
    commend = list(input().split())

    if commend[0] == "push_back":
        result.append(commend[1])
    elif commend[0] == "pop_back":
        result.pop()
    elif commend[0] == "size":
        print(len(result))
    elif commend[0] == "get":
        print(result[int(commend[1])-1])
        