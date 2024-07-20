import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * 1_000_001

    for i in range(k):
        command, n = list(input().split())
        n = int(n)

        if command == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            visited[i] = True
        elif command == 'D':
            if n == -1:
                # visited가 False라면 해당 노드가 삭제된 상태 (동기화를 하기 위함)
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
