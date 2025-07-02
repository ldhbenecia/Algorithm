def dfs(v):
    parent[v] = -9  # 제거할 노드를 -9로 지정
    for i in range(n):
        if (
            v == parent[i]
        ):  # 지울 노드를 부모로 가지고 있는 값들을 찾아서 dfs를 돌려서 재귀적으로 찾아서 제거함
            dfs(i)


n = int(input())
parent = list(map(int, input().split()))
delete = int(input())

dfs(delete)  # 제거할 노드를 부모로 가지고 있는 노드 값들을 모두 제거

# 삭제될 노드들은 전부 -9로 갱신되었음
# -9가 아니고, 다른 노드의 부모 노드가 아닌 값을 찾으면 counting
result = 0
for i in range(n):
    if parent[i] != -9 and i not in parent:
        result += 1

print(result)
