import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
A = deque(list(map(int, input().split()))) # 벨트 내구도 초기화
robot = deque([False] * n) # 로봇이 없는 상태 초기화
answer = 0

while True:
  answer += 1
  
  # 1.컨베이어 벨트 회전 및 로봇 이동
  A.rotate(1)
  robot.rotate(1)
  
  # 로봇이 N(내리는 위치)에 달하면 바로 내림
  robot[n - 1] = False
  
  # 2. 가장 먼저 벨트에 올라간 로봇부터 이동 가능하면 이동
  # n - 1은 내리는 위치이기 때문에 그 전 값부터 반대 방향으로 순회(가장 먼저 벨트에 올라간 로봇)
  for i in range(n - 2, -1, -1):
    # 이동 가능 조건: 로봇이 비어있고, 내구도가 1 이상
    if robot[i] and not robot[i + 1] and A[i + 1] > 0:
      robot[i] = False
      robot[i + 1] = True
      A[i + 1] -= 1
  
  # 로봇이 N(내리는 위치)에 달하면 바로 내림
  robot[n - 1] = False
  
  # 3. 올리는 위치 내구도가 0이 아니면 올리는 위치에 로봇 올림
  if A[0] > 0:
    robot[0] = True
    A[0] -= 1
  
  # 4. 내구도 0인 칸의 개수가 k개 이상이라면 종료, 그렇지 않으면 1번으로 돌아감
  if A.count(0) >= k:
    break

print(answer)