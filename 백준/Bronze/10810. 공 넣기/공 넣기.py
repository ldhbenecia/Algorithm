n, m = map(int, input().split())
basket = [0] * n

for _ in range(m):
  i, j, k = map(int, input().split())
  for ball in range(i, j + 1):
    basket[ball - 1] = k

for i in basket:
  print(i, end=" ")