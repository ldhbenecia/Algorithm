from collections import deque

MAX = 100001


def bfs():
    queue = deque([n])
    visited = [False] * MAX
    visited[n] = True
    dist = [-1] * MAX

    while queue:
        current = queue.popleft()

        # base
        if current == k:
            break

        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next < MAX and not visited[next]:
                visited[next] = True
                dist[next] = current
                queue.append(next)

    # 경로 역추적
    path = []  # 경로 담을 리스트
    pos = k  # 시작 위치
    while pos != -1:  # -1이 나오기전까지 추적 (뒤로 돌아가기)
        path.append(pos)
        pos = dist[pos]

    path.reverse()
    return len(path) - 1, path  # 시작 지점은 time에 미포함하므로 -1


n, k = map(int, input().split())

cnt, path = bfs()
print(cnt)
print(*path)
