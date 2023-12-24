# N = 2, 4, 8, 16, 32, 128
# 재귀 가능

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def dfs(x, y, n):
  global white, blue
  is_same = True
  
  for i in range(x, x + n):
    for j in range(y, y + n):
			# 전부 0이나 1인 그래프가 아닐 시 사분면 탐색 시행
      if graph[x][y] != graph[i][j]:
        is_same = False
        break
  
	# 전부 0이나 1일 시 0이나 1 출력    
  if is_same:
    if graph[x][y] == 0:
      white += 1
    else:
      blue += 1
  else:
    n = n // 2
    dfs(x, y, n)
    dfs(x, y + n, n)
    dfs(x + n, y, n)
    dfs(x + n, y + n, n)
       
dfs(0, 0, n)
print(white) # White
print(blue) # Blue