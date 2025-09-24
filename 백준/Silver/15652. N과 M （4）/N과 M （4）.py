def backtracking(depth, start):
    # base
    if depth == m:
        print(*temp)
        return

    for i in range(start, n + 1):
        temp.append(i)
        backtracking(depth + 1, i)
        temp.pop()


n, m = map(int, input().split())
temp = []
backtracking(0, 1)
