from collections import deque   

def solution(maps):
    answer = 0
    
    a = len(maps)
    b = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(start_x, start_y, end_x, end_y):
        queue = deque([(start_x, start_y, 0)])
        visited = [[False] * b for _ in range(a)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y, time = queue.popleft()
            
            if x == end_x and y == end_y:
                return time
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1))
                        
        return -1
    
    for i in range(a):
        for j in range(b):
            if maps[i][j] == 'S':
                sx, sy = i, j
            if maps[i][j] == 'L':
                lx, ly = i, j
            if maps[i][j] == 'E':
                ex, ey = i, j
            
    find_lever = bfs(sx, sy, lx, ly)
    escape = bfs(lx, ly, ex, ey)
    
    if find_lever == -1 or escape == -1:
        return -1
    
    return find_lever + escape