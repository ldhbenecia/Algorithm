n, current_x, current_y = tuple(map(int, input().split()))

graph = [
 list(map(int, input().split()))
 for _ in range(n)   
]

current_x -= 1
current_y -= 1

visited_num = []
visited_num.append(graph[current_x][current_y])

# 4 2 2 입력했다고 가정
# 시작 위치 (2, 2), 격자 사이즈 4 * 4

# 우선순위(상, 하, 좌, 우)대로 배열 순서 지정
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
  return 0 <= x and x < n and 0 <= y < n


done = True

# 움직이는 코드 
while True:
  for dx, dy in zip(dxs, dys):
    next_x, next_y = current_x + dx, current_y + dy
  
    if in_range(next_x, next_y) and graph[next_x][next_y] > graph[current_x][current_y]:
      current_x, current_y = next_x, next_y
      visited_num.append(graph[current_x][current_y])
      done = False
      break
    
  if done:
    break

  done = True

for i in visited_num:
  print(i, end = ' ')
