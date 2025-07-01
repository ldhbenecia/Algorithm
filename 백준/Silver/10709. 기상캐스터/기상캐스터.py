h, w = map(int, input().split())
board = [input() for _ in range(h)]

for i in range(h):
    result = []
    time = -1
    for j in range(w):
        if board[i][j] == "c":
            time = 0
            result.append(time)
        else:
            if time == -1:
                result.append(-1)
            else:
                time += 1
                result.append(time)
    print(*result)
