def dfs(v):
    stack = []
    stack.append(v)
    visited[v] = True

    while stack:
        v = stack.pop()
        nv = nums[v]

        if not visited[nv]:
            stack.append(nv)
            visited[nv] = True


T = int(input())

for _ in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    result = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)
