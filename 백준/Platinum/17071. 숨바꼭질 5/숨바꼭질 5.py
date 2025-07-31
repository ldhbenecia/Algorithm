from collections import deque

MAX = 500001

# visited[position][time_parity] => 홀짝 시간에 이 위치를 방문했는지 여부
# time_parity: 0이면 짝수 시간, 1이면 홀수 시간
visited = [[False, False] for _ in range(MAX + 1)]


def bfs(n, k):
    queue = deque()
    queue.append((n, 0))  # (현재 위치, 현재 시간)

    visited[n][0] = True  # 시작 위치는 짝수 시간(0초)에 방문 처리

    time = 0
    while True:
        # 동생 위치 계산
        k_pos = k + time * (time + 1) // 2
        if k_pos > MAX:
            return -1  # 더 이상 따라갈 수 없음

        # 해당 시간 parity에 수빈이가 그 위치에 도달한 적 있다면 잡을 수 있음
        if visited[k_pos][time % 2]:
            return time

        # 현재 시간(time)에 수빈이가 도달 가능한 위치들 순회
        for _ in range(len(queue)):
            current, t = queue.popleft()
            if current == k_pos:
                return time

            for next in [current - 1, current + 1, current * 2]:
                if 0 <= next < MAX:
                    parity = (t + 1) % 2  # 다음 시간의 홀짝 구분

                    # 다음 위치에 해당 시간 parity로 처음 방문이라면 큐에 추가
                    if not visited[next][parity]:
                        visited[next][parity] = True
                        queue.append((next, t + 1))
        time += 1  # 다음 시간으로 진행


n, k = map(int, input().split())
print(bfs(n, k))
