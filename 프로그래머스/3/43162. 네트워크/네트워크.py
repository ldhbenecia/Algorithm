from collections import deque

def bfs(start, visited, n, computers):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, n, computers)
            answer += 1
    return answer