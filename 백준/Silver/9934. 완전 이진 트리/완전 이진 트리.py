import sys
input = sys.stdin.readline

def inorder(nums, level):
  if not nums:
    return
  
  mid = len(nums) // 2
  tree[level].append(nums[mid])
  inorder(nums[:mid], level + 1) # 왼쪽 서브트리
  inorder(nums[mid + 1:], level + 1) # 오른쪽 서브트리
  

k = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(k)]

inorder(nums, 0)

for i in tree:
  print(*i)
