n, m = map(int, input().split())

result = []

def dfs(start):
  if len(result) == m:
    print(*result)
    return
  
  for i in range(start, n + 1):
    if i not in result:
      result.append(i)
      dfs(i + 1)
      result.pop()
    
dfs(1)