import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
baseball = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

count = 0

for _ in range(n):
  num, s, b = map(int, input().split())
  prediction = []
  
  for i in baseball:
    strike, ball = 0, 0
    
    for j, str_num in enumerate(str(num)):
      if int(str_num) == i[j]:
        strike += 1
      if int(str_num) != i[j] and int(str_num) in i:
        ball += 1
    
    if s == strike and b == ball:
      prediction.append(i)
      
  baseball = prediction

print(len(baseball))