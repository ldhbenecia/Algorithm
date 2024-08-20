from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    group = [(x, y)] # 개통 가능한 좌표 저장 리스트

    visited[x][y] = True
    total = graph[x][y] # 초기 값 (0, 0) 위치 값

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    group.append((nx, ny))
                    total += graph[nx][ny]
    
    # 인구 이동이 있었을 경우
    if len(group) > 1:
        renew = total // len(group)
        for i, j in group:
            graph[i][j] = renew
        return True
    
    return False

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 조건: 동서남북으로 근접한 숫자와의 차이가 L <= diff <= R이라면 개통
# 개통을 하면 result += 1
# 개통을 아무데도 안하면 0임

# 개통할 수 있을 때 까지 개통하고 (While True)
# 개통을 못할때 끝내고 그때 기준으로 인구이동 몇 번 했는지 체크

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
    visited = [[False] * (n) for _ in range(n)]
    move = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j): # 인구이동이 있었는 지 판단
                    move = True

    if not move:
        break

    time += 1

print(time)
