from collections import deque


def bfs():
    queue = deque([n])
    visited = [0] * 100001
    time, cnt = 0, 0

    while queue:
        current = queue.popleft()

        # base
        # 동생의 위치에 도달했으면
        if current == k:
            time = visited[current]  # 결과 값은 현재 위치
            cnt += 1
            continue

        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next < 100001 and (
                visited[next] == 0 or visited[next] == visited[current] + 1
            ):
                visited[next] = visited[current] + 1
                queue.append(next)

    return time, cnt


n, k = map(int, input().split())

time, cnt = bfs()
print(time)
print(cnt)
