n, m, x, y, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 동 서 북 남 (문제 조건)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6


def turn(dir):
    top, bottom, front, back, left, right = dice  # 1 6 5 2 4 3
    if dir == 1:  # 동 (4 3 5 2 6 1)
        dice[0], dice[1], dice[4], dice[5] = left, right, bottom, top
    elif dir == 2:  # 서 (3 4 5 2 1 6)
        dice[0], dice[1], dice[4], dice[5] = right, left, top, bottom
    elif dir == 3:  # 북 (5 2 6 1 4 3)
        dice[0], dice[1], dice[2], dice[3] = front, back, bottom, top
    elif dir == 4:  # 남 (2 5 1 6 4 3)
        dice[0], dice[1], dice[2], dice[3] = back, front, top, bottom


command = list(map(int, input().split()))

for i in command:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]
    if 0 <= nx < n and 0 <= ny < m:
        turn(i)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[1]  # 주사위 바닥면에 쓰여 있는 수가 칸에 복사
        else:
            dice[1] = graph[nx][ny]  # 숫자가 있으면 주사위 아랫면에 복사
            graph[nx][ny] = 0  # 칸에 쓰여있는 숫자는 0
        print(dice[0])
        x, y = nx, ny
