from collections import deque

n, m = map(int, input().split())
idx = map(int,input().split())
dq = deque([i for i in range(1, n+1)])
count = 0

for i in idx:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2: # 뽑아야 하는 수의 위치에 따른 식 (왼쪽으로) 
                while dq[0] != i:
                    dq.append(dq.popleft()) # dq의 왼쪽이라면 왼쪽(앞 쪽)의 값을 빼서 뒤로 보내는 것이 빠름
                    count += 1
            else: # 오른쪽으로 
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1
                    
print(count)