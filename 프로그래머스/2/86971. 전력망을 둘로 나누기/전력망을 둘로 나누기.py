from collections import deque

def bfs(graph, visited, start, remove):
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i] and i != remove:
                visited[i] = True
                queue.append(i)
                count += 1
    
    return count

def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
        
    for i, j in wires:
        visited = [False] * (n + 1)
        network1 = bfs(graph, visited, i, j)
        network2 = bfs(graph, visited, j, i)
        answer = min(answer, abs(network1 - network2))
    
    return answer