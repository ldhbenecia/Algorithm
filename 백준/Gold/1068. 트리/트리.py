def dfs(erase):
    node[erase] = -2
    
    for i in range(n):
        if erase == node[i]:
            dfs(i)

n = int(input())
node = list(map(int, input().split()))
erase = int(input())

dfs(erase)

cnt = 0
for i in range(n):
    if node[i] != -2 and i not in node:
        cnt += 1
        
print(cnt)