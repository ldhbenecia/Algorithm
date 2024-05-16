k = int(input())

def hanoi(n, left, mid, right):
  
  if n == 1:
    print(left, right)
    return
  else:
    hanoi(n - 1, left, right, mid)
    print(left, right)
    hanoi(n - 1, mid, left, right)
  
print(2**k - 1)

if k <= 20:
  hanoi(k, 1, 2, 3)