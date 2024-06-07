from collections import deque   

def solution(maps):
    answer = 0
    
    a = len(maps)
    b = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def find_lever(x, y):
        queue = deque([(x, y, 0)])
        visited = [[False] * b for _ in range(a)]
        visited[x][y] = True
        
        while queue:
            x, y, time = queue.popleft()
            
            if maps[x][y] == 'L':
                return (x, y, time)
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1))
                        
        return -1, -1, -1
    
    def escape(x, y, time):
        queue = deque([(x, y, time)])
        visited = [[False] * b for _ in range(a)]
        visited[x][y] = True
        
        while queue:
            x, y, time = queue.popleft()
            
            if maps[x][y] == 'E':
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
                lever_x, lever_y, time = find_lever(i, j)
                return escape(lever_x, lever_y, time)
    return -1