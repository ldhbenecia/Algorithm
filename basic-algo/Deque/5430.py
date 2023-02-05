from collections import deque

t = int(input())

for i in range(t):
  p = input() # 함수
  n = int(input()) # 배열에 들어있는 수의 개수
  num = input()[1:-1].split(",") # 정수 배열
  queue = deque(num)
  
  flag = 0
  
  if n == 0:
    queue = [] # deque의 ['']는 길이를 1로 취급하기 때문에 빈 배열로 초기화 필요
  
  for j in p:
    if j == "R":
      flag += 1
      
    elif j == "D":
      if len(queue) == 0:
        print("error")
        break
      else: # 여기서 시간복잡도를 줄이는 방법
        if flag % 2 == 1: # R이 한번 나왔을 경우 flag는 1인 상태
          queue.pop()
        else: # R이 두번 나왔을 경우 flag는 2인 상태 (짝수), 이 경우 뒤집고 뒤집는 것이기 때문에 변화가 없음
          queue.popleft()
          
  else:
    if flag % 2 == 1:
      queue.reverse() # 출력할 때 R이 1번 나왔을 경우 reverse 이후 출력
    print("[" + "," .join(queue) + "]")


# 예시 1) RDD [1,2,3,4] 일 떄
# R이 한번 나와서 뒤집어지므로 4,3,2,1
# DD 하면 2,1이 남는다. -> R이 1번일 경우 pop()을 두번 치면 1,2가 남고 이때 reverse 처리 후 출력

# 예시 2) RRD [1,2,3,4] 일 때
# R이 두번 나와서 뒤집어져도 그대로 1,2,3,4
# D 하면 2,3,4 -> popleft() 처리 후 출력