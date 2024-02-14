import math

def is_prime(num):
  if num == 1:
    return False
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True
    
t = int(input())

for i in range(t):
  num = int(input())
  a, b = num // 2, num // 2
  
  while a > 0:
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1
