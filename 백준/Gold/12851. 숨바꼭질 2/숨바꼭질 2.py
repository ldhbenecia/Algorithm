from collections import deque

def bfs(a, b):
    queue = deque([(a, 0)]) # 출발 지점, 시간
    fast = 1e9
    cnt = 0

    while queue:
        position, time = queue.popleft()
        visited[position] = True

        # base 조건
        if position == b and time <= fast:
            cnt += 1
            fast = time
        if time > fast:
            break

        for i in [position * 2, position - 1, position + 1]:
            if 0 <= i <= 100000 and not visited[i]:
                queue.append((i, time + 1))

    return fast, cnt

n, k = map(int, input().split())
visited = [False] * 100001

fast, kind = bfs(n, k)

print(fast)
print(kind)
