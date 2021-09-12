m, n = map(int, input().split())
board = []
repair = []

for _ in range(m):
    board.append(input())

for i in range(m-7): # 행 고정
    for j in range(n-7): # 열 고정
        first_w = 0
        first_b = 0
        for k in range(i, i+8):
            for x in range(j, j+8):
                if (k+x) % 2 == 0:
                    if board[k][x] != "W":
                        first_w = first_w+1
                    if board[k][x] != "B":
                        first_b = first_b+1
                else:
                    if board[k][x] != "B":
                        first_w = first_w+1
                    if board[k][x] != "W":
                        first_b = first_b+1

        repair.append(first_w)
        repair.append(first_b)


print(min(repair))