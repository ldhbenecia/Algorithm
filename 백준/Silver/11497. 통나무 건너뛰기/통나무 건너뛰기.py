t = int(input())

for _ in range(t):
  n = int(input())
  tree = list(map(int, input().split()))
  tree.sort()
  
  left = []
  right = []
  for i in range(0, n, 2):
    left.append(tree[i])
  for i in range(1, n, 2):
    right.append(tree[i])
  right.sort(reverse=True)
  
  trees = left + right
  
  result = 0
  for i in range(n):
    result = max(result, abs(trees[i] - trees[i-1]))
  
  print(result)
    