n, r, c = map(int, input().split())
start = 0

while n > 1:
  half_size = (2 ** n) // 2
  
  if r < half_size and c < half_size: # 2사분면
    pass
  
  elif r < half_size and half_size <= c: # 1사분면
    start += half_size ** 2
    c -= half_size
    
  elif half_size <= r and c < half_size: # 3사분면
    start += half_size ** 2 * 2
    r -= half_size
    
  elif half_size <= r and half_size <= c: # 4사분면
    start += half_size ** 2 * 3
    r -= half_size
    c -= half_size
    
  n -= 1

if r == 0 and c == 0:
  print(start)
if r == 0 and c == 1:
  print(start + 1)
if r == 1 and c == 0:
  print(start + 2)
if r == 1 and c == 1:
  print(start + 3)