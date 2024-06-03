import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

min_time = 1e9
height = 0
for floor in range(257):
  plus, minus = 0, 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] < floor:
        plus += floor - graph[i][j]
      else:
        minus += graph[i][j] - floor
        
  # 인벤토리에 있는 걸로 커버가 안될 경우 continue
  if plus > minus + b:
    continue
  
  # 인벤토리에 있는 블록과 깎아낸 블록으로 채울 수 있는 경우
  time = minus * 2 + plus
  
  # 시간이 더 적거나, 시간이 같다면 더 높은 높이를 선택
  if time <= min_time:
    min_time = time
    height = floor
  
print(min_time, height)  