from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, room):
    queue = deque([(x, y, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    
    while queue:
        sx, sy, dist = queue.popleft()
        
        # 맨헤튼 거리 2 = 탐색 안함
        if dist == 2:
            continue
        
        for i in range(4):
            nx = dx[i] + sx
            ny = dy[i] + sy
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                
                # 파티션이 발견되으니 탐색 안함(이 방향 막힘)
                if room[nx][ny] == 'X':
                    continue
                
                # 거리두기 어김
                if room[nx][ny] == 'P':
                    return False
                
                queue.append((nx, ny, dist + 1))
        
    return True

def check(room):
    for r in range(5):
        for c in range(5):
            if room[r][c] == 'P':
                if not bfs(r, c, room):
                    return 0
    return 1
            
def solution(places):
    answer = []
    for room in places:
        answer.append(check(room))
    
    return answer