import sys

input = sys.stdin.readline


# 0: 빈 칸, 6: 벽, 1~5: CCTV

# CCTV 1 ~ 5번 당 감시 가능한 위치 판별 필요
# 감시할 수 있는 영역 #

# CCTV 1번부터 5번까지 각각의 CCTV가 감시할 수 있는 영역을 #으로 칠하기
# CCTV는 CCTV를 통과할 수 있음

# 문제를 보고 바로 떠오른 알고리즘 도식도
# 1. 입력 값에 대해 벽(6), 빈칸(0), CCTV 1번부터 각각 CCTV의 GRAPH 5개의 맵 생성
# 1-1. 없는 번호의 CCTV의 맵은 그냥 벽만 두고 미처리
# 2. 각각의 CCTV의 맵 1, 2, 3, 4, 5에서 감시영역을 두자.
# 3. 이 맵 5개를 비교하면서 감시할 수 있는 영역을 전부 #으로 칠하자.
# 4. 감시할 수 없는 영역 사각지대의 최소 크기 (최대한 많은 영역 감시)
# 4-1. 이걸 위해서는 각각의 CCTV맵에서 감시할 수 있는 영역 #에 대한 카운트를 센다.
# 4-2. #의 카운트를 센 다음 CCTV를 회전해가면서 #의 카운트를 또 센다.
# 4-3. #의 카운트가 가장 많은 영역으로 맵을 선정
# 5. 이거 좀 많이 비효율적인 것 같은데 일단 풀이 시작

# 6. 번호별 맵 5개 생성 -> 비교는 비효율적임
# 7. 한 지도에서 감시마킹/원상복구를 백트래킹을 통해 탐색

# cctv 90도 회전 가능 (동: 0, 남: 1, 서: 2, 북: 3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 각 CCTV별 감시 가능 영역
cctv_dir = {
    1: [[0], [1], [2], [3]],  # 동 남 서 북
    2: [[0, 2], [1, 3]],  # 동+서, 남+북
    3: [[0, 3], [0, 1], [2, 3], [2, 1]],  # 동+북, 동+남, 서+북, 서+남
    4: [
        [0, 3, 2],
        [1, 0, 3],
        [2, 1, 0],
        [3, 2, 1],
    ],  # 동+북+서, 남+동+북, 서+남+동, 북+서+남
    5: [[0, 1, 2, 3]],  # 동+남+서+북
}

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctvs.append((i, j, graph[i][j]))  # 좌표, CCTV 번호 저장


# 한 방향 직선으로 감시 표시. 새로 표시한 좌표만 반환 (원복용)
def mark(r, c, dir):
    """
    (r,c)에서 방향 d로 직선으로 쭉 진행하며:
    - 벽(6)을 만나면 중단
    - CCTV(1~5), 이미 감시된 칸(7)은 통과
    - 빈칸(0)만 7로 바꾸고, 그 좌표를 changed에 기록
    반환: 이번 호출에서 새로 바꾼 좌표 리스트
    """
    changed = []
    nr = r + dx[dir]
    nc = c + dy[dir]

    while 0 <= nr < n and 0 <= nc < m:
        if graph[nr][nc] == 6:
            break

        if graph[nr][nc] == 0:
            graph[nr][nc] = 7  # 7로 MARK
            changed.append((nr, nc))

        nr += dx[dir]
        nc += dy[dir]

    # print("마킹한 영역", changed)
    return changed


result = 1e9  # 사각지대 개수


def backtracking(depth):
    global result

    # base
    if depth == len(cctvs):
        temp = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    temp += 1
        result = min(result, temp)
        # print("결과 창", result)
        return

    r, c, t = cctvs[depth]  # CCTV 행, 열, 번호

    # CCTV 1번부터 5번까지 graph에 있는 거 감시 가능영역 MARK
    for dir_set in cctv_dir[t]:
        total_changed = []  # 새로 마킹한 좌표 저장 리스트

        # 현재 CCTV의 가능한 모든 방향 회전해가면서 마킹
        for dir in dir_set:  # 이 CCTV가 감시 가능한 영역 dx, dy
            total_changed.extend(mark(r, c, dir))

        # 다음 번호 CCTV MARK
        backtracking(depth + 1)

        # 복귀: 이번 단계에서 새로 바꾼 칸만 원복
        # print("복구 시키기전 토탈 체인지", total_changed)
        for ii, jj in total_changed:
            graph[ii][jj] = 0


backtracking(0)
print(result)
