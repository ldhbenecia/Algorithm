from collections import deque


def bfs(a, b):
  queue = deque([(a, 0)])
  shortest_time = 100000
  count = 0

  while queue:
    position, time = queue.popleft()
    visited[position] = 1

    if position == b and time <= shortest_time:
      shortest_time = time
      count += 1
    if time > shortest_time:
      break
    
    for i in [position - 1, position + 1, position * 2]:
      if 0 <= i <= 100000 and not visited[i]:
        queue.append((i, time + 1))

  return shortest_time, count

n, k = map(int, input().split())
visited = [0] * 100001

shortest_time, num_ways = bfs(n, k)
print(shortest_time)
print(num_ways)
