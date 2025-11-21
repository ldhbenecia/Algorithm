from collections import deque


def bfs():
    queue = deque([S])
    visited[S] = 0

    while queue:
        cur = queue.popleft()

        # base
        if cur == G:
            return visited[cur]
        else:
            for goal in (cur + U, cur - D):
                if 1 <= goal <= F and visited[goal] == -1:
                    visited[goal] = visited[cur] + 1
                    queue.append(goal)

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)

if S == G:
    print(0)
else:
    print(bfs())
