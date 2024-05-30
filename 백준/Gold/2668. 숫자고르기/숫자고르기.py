def dfs(start, current):
  stack = [(start, current)]
  path = set()

  while stack:
    first, second = stack.pop()
    if not visited[second]:
      visited[second] = True
      path.add(second)
      stack.append((first, graph[second]))
    elif second == start:
      result.update(path)
      return

n = int(input())
graph = [0] + [int(input()) for _ in range(n)]

result = set()  # result를 set으로 초기화하여 중복 제거
for i in range(1, n + 1):
  visited = [False] * (n + 1)
  dfs(i, i)

print(len(result))
for i in sorted(result):
  print(i)
