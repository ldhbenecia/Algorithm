import sys

input = sys.stdin.readline


def backtracking(depth):
    # base
    if depth == m:
        print(*temp)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            if temp and i + 1 <= temp[-1]:
                continue
            visited[i] = True
            temp.append(i)
            backtracking(depth + 1)
            temp.pop()
            visited[i] = False


n, m = map(int, input().split())
temp = []
visited = [False] * (n + 1)
backtracking(0)
# 완전탐색 -> 중복되는 수는 걸러줘야함 -> 백트래킹
