import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

start = 0
end = tree[-1]

while start <= end:
  mid = (start + end) // 2
  temp = 0
  for i in tree:
    if mid < i:
      temp += i - mid

  if temp < m:
    end = mid - 1
  else:
    start = mid + 1
    
print(end)