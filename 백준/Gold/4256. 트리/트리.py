def postorder(root, start, end):
  for i in range(start, end):
    if preorder[root] == inorder[i]:
      postorder(root + 1, start, i) # left
      postorder(root + (i - start) + 1, i + 1, end) # right
      postorder_list.append(preorder[root])

t = int(input())

for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder_list = []
    postorder(0, 0, n)
    
    print(*postorder_list)
