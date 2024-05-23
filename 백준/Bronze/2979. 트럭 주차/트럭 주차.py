import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
time = [0] * 101

for _ in range(3):
  a, b = map(int, input().split())
  
  for i in range(a, b):
    time[i] += 1
    
answer = 0
for i in time:
  if i == 1:
    answer += i * A
  if i == 2:
    answer += i * B
  if i == 3:
    answer += i * C
    
print(answer)