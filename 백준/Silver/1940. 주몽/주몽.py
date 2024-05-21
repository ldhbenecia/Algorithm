import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ingredients = sorted(list(map(int, input().split())))

count = 0
start = 0
end = n - 1

while start < end:
  if ingredients[start] + ingredients[end] == m:
    count += 1
    start += 1
  elif ingredients[start] + ingredients[end] < m:
    start += 1
  else:
    end -= 1
    
print(count)