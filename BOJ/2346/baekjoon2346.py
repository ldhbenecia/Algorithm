from collections import deque

n = int(input())
# 튜플 형태로 인덱스와 인덱스에 해당하는 값을 동시 저장
queue = deque(enumerate(map(int, input().split())))
result = [] # 풍선이 터진 index를 담을 리스트

while queue:
    temp = queue.popleft() # 첫 번째 요소 pop
    result.append(temp[0]+1)
    
    if temp[1] > 0:
        queue.rotate(-(temp[1]-1))
    elif temp[1] < 0:
        queue.rotate(-temp[1])
        
print(' '.join(map(str, result)))