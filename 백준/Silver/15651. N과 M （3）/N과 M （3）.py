n, m = map(int, input().split())

result = []
def backtracking():
  if len(result) == m:
    print(*result)
    return
    
  for i in range(1, n + 1):
    result.append(i)
    backtracking()
    result.pop()
    
backtracking()