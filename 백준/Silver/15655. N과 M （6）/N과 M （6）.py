n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

result = []

def backtracking(start):
  if len(result) == m:
    print(*result)
    return
  
  for i in range(start, len(num)):
    if num[i] not in result:
      result.append(num[i])
      backtracking(i + 1)
      result.pop()
      
backtracking(0)