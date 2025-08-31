from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]  # 0: 빈칸, 1: 뱀, 2: 사과

for _ in range(k):
    col, row = map(int, input().split())
    graph[col - 1][row - 1] = 2  # apple

l = int(input())
direction_change = dict()
for _ in range(l):
    x, c = input().split()
    direction_change[int(x)] = c

dx = [-1, 1, 0, 0]  # 북(0) 남(1) 서(2) 동(3)
dy = [0, 0, -1, 1]
direction = 3

snake = deque([(0, 0)])
graph[0][0] = 1  # 뱀 시작 위치

time = 0
x, y = 0, 0  # 벰 현재 좌표

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽이나 자기 몸에 부딫히면 종료
    if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 1:
        print(time)
        break

    # 사과를 먹으면 몸 늘림
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        snake.appendleft((nx, ny))
    else:
        # 사과가 없으면 꼬리 빼고 이동
        graph[nx][ny] = 1
        snake.appendleft((nx, ny))
        tx, ty = snake.pop()  # 꼬리 빼기
        graph[tx][ty] = 0  # 그래프 동기화

    x, y = nx, ny

    # 딕셔너리에 등록해놓은 시간이 되면 방향 전환
    # 북 남 서 동
    if time in direction_change:
        if direction_change[time] == "L":
            direction = [2, 3, 1, 0][direction]
        elif direction_change[time] == "D":
            direction = [3, 2, 0, 1][direction]
