from collections import deque

def solution(board):
    answer = 0
    
    a = len(board)
    b = len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * b for _ in range(a)]
    
    def bfs(x, y):
        queue = deque([(x, y, 0)])
        visited[x][y] = True

        while queue:
            x, y, time = queue.popleft()
            
            if board[x][y] == 'G':
                return time

            for i in range(4):
                nx, ny = x, y
                
                # 해당 방향으로 끝까지 이동
                while 0 <= nx + dx[i] < a and 0 <= ny + dy[i] < b and board[nx + dx[i]][ny + dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]

                if not visited[nx][ny]:
                    queue.append((nx, ny, time + 1))
                    visited[nx][ny] = True

        return -1
    
    for i in range(a):
        for j in range(b):
            if board[i][j] == "R":
                return bfs(i, j)
                
    return -1