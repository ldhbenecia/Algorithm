from collections import deque

def left(num, direction):
  if num < 0:
    return
  if gear[num][2] != gear[num + 1][6]:
    left(num - 1, -direction)
    gear[num].rotate(direction)
    
def right(num, direction):
  if num > 3:
    return
  if gear[num - 1][2] != gear[num][6]:
    right(num + 1, -direction)
    gear[num].rotate(direction)
  
gear = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
  num, direction = map(int, input().split()) # num: 1, 2, 3, 4
  num -= 1 # 인덱스를 위해 0, 1, 2, 3
  
  left(num - 1, -direction)
  right(num + 1, -direction)
  gear[num].rotate(direction)
  
score = 0

if gear[0][0] == 0:
  score += 0
else:
  score += 1
  
if gear[1][0] == 0:
  score += 0
else:
  score += 2
  
if gear[2][0] == 0:
  score += 0
else:
  score += 4
  
if gear[3][0] == 0:
  score += 0
else:
  score += 8

print(score)