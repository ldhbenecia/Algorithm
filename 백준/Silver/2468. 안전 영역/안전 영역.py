from collections import deque

def bfs(x, y, height):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# graph에 있는 숫자 중 최대 값을 찾아서 0 ~ 최댓값까지 전부 돌려서 안전한 영역이 가장 많은 값을 찾기
max_height = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > max_height:
            max_height = graph[i][j]
            
result = []        
for height in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > height:
                bfs(i, j, height)
                safe += 1
    result.append(safe)
    
print(max(result))
