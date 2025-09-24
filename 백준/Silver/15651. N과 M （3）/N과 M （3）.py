def backtracking(depth):
    if depth == m:
        print(*temp)
        return
    for i in range(1, n + 1):
        temp.append(i)
        backtracking(depth + 1)
        temp.pop()


n, m = map(int, input().split())
temp = []
backtracking(0)
