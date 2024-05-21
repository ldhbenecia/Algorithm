import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

max_value = sum(temperature[:k])
value = max_value

for i in range(k, n):
  value += temperature[i]
  value -= temperature[i - k]
  
  if value > max_value:
    max_value = value
  
print(max_value)