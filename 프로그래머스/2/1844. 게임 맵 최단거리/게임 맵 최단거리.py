from collections import deque

def bfs(x, y, maps):
    queue = deque([(x, y)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    return maps[-1][-1] if maps[-1][-1] != 1 else -1
                

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer
