from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [], # 노드의 번호가 1번부터 시작하는 경우가 많기 때문에 index 0에 대한 정보는 비워둘 수 있도록 함
    [2, 3, 8], # 1번 index부터 해당 노드의 인접한 노드가 무엇인지 달아줌
    [1, 7],
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9 
# 처음에는 모든 노드를 아직 방문하지 않은 상태 설정
# index 0은 사용하도록 하지 않기 위해서 하나 더 큰 크기로 1차원 리스트를 초기화

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

#실행결과 :: 1 2 3 8 7 4 5 6