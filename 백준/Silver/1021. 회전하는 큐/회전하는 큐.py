from collections import deque

n, m = map(int, input().split())
position = list(map(int, input().split()))

queue = deque([i for i in range(1, n + 1)])
result = 0

for pos in position:
    idx = queue.index(pos)

    if idx < len(queue) / 2:  # 왼쪽으로 회전
        while queue[0] != pos:
            queue.append(queue.popleft())
            result += 1
    else:  # 오른쪽으로 회전
        while queue[0] != pos:
            queue.appendleft(queue.pop())
            result += 1
    queue.popleft()

print(result)
