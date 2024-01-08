n, m = map(int, input().split())

result = []
def backtracking(start):
  if len(result) == m:
    print(*result)
    return 

  for i in range(start, n + 1):
    result.append(i)
    backtracking(i)
    result.pop()
    
backtracking(1)