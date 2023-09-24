from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] * (n + 1)
    
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[current] + 1
    
    max_num = max(distance)
    for i in distance:
        if i == max_num:
            answer += 1
    return answer
