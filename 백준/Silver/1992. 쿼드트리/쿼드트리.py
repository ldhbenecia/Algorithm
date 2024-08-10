def quard(row, col, size):
    is_same = True

    for i in range(row, row + size):
        for j in range(col, col + size):
            if graph[row][col] != graph[i][j]:
                is_same = False
                break

    # 해당 영역(사분면)이 1이거나 0인지 판별
    if is_same:
        print(graph[row][col], end = '')
    else:
        half_size = size // 2
        print("(", end = '')
        quard(row, col, half_size) # 왼쪽 위
        quard(row, col + half_size, half_size) # 오른쪽 위
        quard(row + half_size, col, half_size) # 왼쪽 아래
        quard(row + half_size, col + half_size, half_size) # 오른쪽 아래
        print(")", end = '')

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

quard(0, 0, n)
