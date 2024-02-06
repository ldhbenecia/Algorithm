t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  a = sorted(list(map(int, input().split())))
  b = sorted(list(map(int, input().split())))
  
  count = 0
  a_start, b_start = 0, 0
  
  while a_start < n and b_start < m:
    if a[a_start] > b[b_start]:
      count += 1
      b_start += 1
      if b_start == m:
        a_start += 1
        b_start = 0
    else:
      a_start += 1
      b_start = 0

  print(count)