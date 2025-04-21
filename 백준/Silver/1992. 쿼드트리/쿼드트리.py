def tree(x, y, n):
    temp = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if temp != board[i][j]:
                temp = -1
                break

    # 전체가 0이거나 1이 아닌 경우
    if temp == -1:
        result.append("(")

        # 절반으로 나눠도 더 분할해야하면 계속 분할
        n //= 2
        tree(x, y, n) # 왼쪽 위
        tree(x, y + n, n) # 오른쪽 위
        tree(x + n, y, n) # 왼쪽 아래
        tree(x + n, y + n, n) # 오른쪽 아래
        result.append(")")

    elif temp == 1:
        result.append("1")
    else:
        result.append("0")


n = int(input())
board = [list(map(int, input())) for _ in range(n)]
result = []
tree(0, 0, n)

result = "".join(result)
print(result)
