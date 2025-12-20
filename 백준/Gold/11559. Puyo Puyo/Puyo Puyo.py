from collections import deque

"""
아래에 바닥이나 다른 뿌요가 나올 때 까지 아래로 떨어짐
같은색 뿌요가 상하좌우로 4개 이상 연결되어있으면 테트리스처럼 한꺼번에 이어진 것들 제거됨 +1연쇄

없어지고 나서 연쇄작업 이후 위에 다른 뿌요들이 있으면 이것들도 차례대로 아래로 떨어짐
이것도 또 터짐, 이걸 반복하면서 연쇄 작용이 일어남

터질 수 있는 뿌요(상하좌우 연결 4개 이상)이 여러 그룹이 있다면 동시에 터져야함
여러 그룹이 터지더라도 한 번의 연쇄가 추가
-> 그래프 탐색을 사용해서 상하좌우로 4개이상 연결된거를 다 한번에 터트림, 한 사이클당 연쇄++;

1. .이 아닌 뿌요를 그래프에서 찾는다.
2. 찾은 뿌요가 상하좌우로 같은 색상으로 4개 이상 연결되었는지 탐색한다.
3. 4개 이상이 탐색이 된다면 터트린다.
4. 터트리고 터진 부분을 아래로 내려서 채워야 한다.
5. 색상이 다르지만 터질 수 있는 그룹이 여러개라면 이것들은 함께 터지며 연쇄는 +1이다.
6. 고로 한번의 그래프 탐색 BFS에서 터질 수 있는걸 터트리고 그 탐색 한 사이클이 끝나면 +1
"""


def bfs(x, y, visited):
    queue = deque([(x, y)]) # 탐색 시작 좌표
    group = [(x, y)]  # 터트릴 뿌요 좌표 저장 그룹

    visited[x][y] = True
    color = graph[x][y]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy

            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    group.append((nx, ny))

    if len(group) >= 4:
        return group
    else:
        return []


def gravity():
    for col in range(6):
        stack = []

        # 아래부터 빈 칸이 아닌 좌표 수집
        for row in range(11, -1, -1):
            if graph[row][col] != ".":
                stack.append(graph[row][col])

        for row in range(11, -1, -1):
            if stack:
                graph[row][col] = stack.pop(0)
            else:
                graph[row][col] = "."


graph = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    bomb = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    bomb.append(group)

    if len(bomb) == 0:
        break

    for group in bomb:
        for x, y in group:
            graph[x][y] = "."

    gravity()
    result += 1

print(result)
