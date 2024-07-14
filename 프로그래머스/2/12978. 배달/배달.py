import heapq

def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distance[start] = 0
        
        while queue:
            dist, now = heapq.heappop(queue)
            
            if distance[now] < dist:
                continue
            
            for i in graph[now]:
                cost = dist + i[1]  # 현재 노드까지의 거리(dist) + 목적지 노드까지의 거리(i[1])
                if cost < distance[i[0]]:  # 새로운 거리가 기존 거리보다 짧다면
                    distance[i[0]] = cost  # 거리 업데이트
                    heapq.heappush(queue, (cost, i[0]))  # 우선순위 큐에 추가
                    
    dijkstra(1)
    
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer