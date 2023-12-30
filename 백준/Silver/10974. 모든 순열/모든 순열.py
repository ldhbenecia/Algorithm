n = int(input())

result = []

def dfs():
  if len(result) == n:
    print(*result)
    return
  
  for i in range(1, n + 1):
    if i not in result:
      result.append(i)
      dfs()
      result.pop()
    
dfs()