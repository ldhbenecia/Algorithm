import sys
input = sys.stdin.readline

def inorder(start, end, idx):
  if start > end:
    return
  
  node = (start + end) // 2
  tree[idx].append(nums[node])
  inorder(start, node - 1, idx + 1) # 왼쪽 서브트리
  inorder(node + 1, end, idx + 1) # 오른쪽 서브트리
  

k = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(k)]

inorder(0, len(nums) - 1, 0)

for i in tree:
  print(*i)
