from collections import deque

n, m = map(int, input().split())
index = list(map(int, input().split()))
data = deque([i for i in range(1, n+1)])

cnt = 0 # 최소값 

for i in index:
  while True:
    if data[0] == i:
      data.popleft()
      break
    else:
      if data.index(i) < len(data) / 2:
        data.rotate(-1)
        cnt += 1
      else:
        data.rotate(1)
        cnt += 1
        
print(cnt)