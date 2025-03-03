from collections import deque
import copy

# 풀이
# 1. 완전 탐색(백트래킹)을 사용하여 빈 칸에 벽을 3개까지 놓는다.
# 2. 벽을 다 놓았으면 바이러스를 퍼뜨려본다.
# 3. 안전 영역의 개수를 센다.
# 4. board 끝까지 이를 반복해가며 어떻게 벽을 쌓았을 때 가장 안전 영역이 큰 지 구한다.


def bfs():
    queue = deque()
    basic_board = copy.deepcopy(board)

    # queue에 바이러스 삽입
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if basic_board[nx][ny] == 0:  # 빈 칸인가? (감염될 수 있는가)
                    basic_board[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    safe_area = 0

    for i in range(n):
        for j in range(m):
            if basic_board[i][j] == 0:
                safe_area += 1

    answer = max(answer, safe_area)


def make_wall(cnt):
    if cnt == 3:  # 벽 다 쌓았으면 바이러스 퍼뜨려보기
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1  # 벽 쌓기
                make_wall(cnt + 1)  # 두 번째 벽 쌓으로 재귀
                board[i][j] = 0  # 벽 3개 다 쌓은 후 허물기


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
make_wall(0)
print(answer)
