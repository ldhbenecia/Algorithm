n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

result = []
def backtracking():
  if len(result) == m:
    print(*result)
    return
  
  for i in range(len(num)):
    if num[i] not in result:
      result.append(num[i])
      backtracking()
      result.pop()
      
backtracking()