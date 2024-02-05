h, w = map(int, input().split())
block = list(map(int, input().split()))
count = 0

for i in range(1, w - 1):
  left_max_height = max(block[:i])
  right_max_height = max(block[i+1:])
  water = min(left_max_height, right_max_height)
  
  if water > block[i]:
    count += water - block[i]
    
print(count)