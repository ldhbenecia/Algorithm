from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        queue.append((nx, ny))
                    if graph[nx][ny] == 1: # 인접하면 치즈 녹이기
                        graph[nx][ny] = 0
                        cnt += 1
                    visited[nx][ny] = True
                    
    history.append(cnt)
    return cnt

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
time = 0
history = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    visited = [[False] * w for _ in range(h)]
    
    melt_cnt = bfs()
    time += 1
    
    if melt_cnt == 0:
        print(time - 1)
        print(history[-2])
        break
