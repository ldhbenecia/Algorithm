n, m = map(int, input().split())
j = int(input())
positions = [int(input()) for _ in range(j)]

count = 0
left = 1
right = m

for position in positions:
  # 사과가 오른쪽에 떨어진다면
  if position > right:
    count += (position - right)
    left += (position - right)
    right = position
    
  # 사과가 왼쪽에 떨어진다면
  elif position < left:
    count += (left - position)
    right -= left - position
    left = position
    
print(count)
