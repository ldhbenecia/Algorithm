def dfs(depth, start, end):
    # base
    if start > end:
        return

    mid = (start + end) // 2
    result[depth].append(tree[mid])

    dfs(depth + 1, start, mid - 1)  # 왼쪽
    dfs(depth + 1, mid + 1, end)  # 오른쪽


k = int(input())
tree = list(map(int, input().split()))

result = [[] for _ in range(k)]
dfs(0, 0, len(tree) - 1)

for i in result:
    print(*i)
