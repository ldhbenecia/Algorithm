import heapq

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
L.sort(key=lambda x:x[0]) # 막대의 왼쪽과 오른쪽 끝 점을 모두 모아 오름차순 정렬 O(nlogn)

heap = []
heapq.heappush(heap, L[0][1]) # 첫 막대 끝점 저장

for i in (1, n): # 선분 탐색
  if heap[0] < L[i][0]:
    heapq.heappop(heap)
  heapq.heappush(heap, L[i][1])
  
print(heap)
print(len(heap))