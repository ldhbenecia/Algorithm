from collections import deque

def solution(maps):
    answer = []
    
    a = len(maps)
    b = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        result = int(maps[x][y])
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        result += int(maps[nx][ny])
                        
        return result
    
    visited = [[False] * b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
    
    if not answer:
        return [-1]
    
    return sorted(answer)