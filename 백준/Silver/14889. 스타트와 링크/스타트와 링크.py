def backtracking(depth, idx):
    global answer
    
    if depth == n // 2:
      start, link = 0, 0
      for i in range(n):
        for j in range(n):
          if visited[i] and visited[j]:
            start += graph[i][j]
          elif not visited[i] and not visited[j]:
            link += graph[i][j]
      answer = min(answer, abs(start - link))
      
    else:
      for i in range(idx, n):
        visited[i] = True
        backtracking(depth + 1, i + 1)
        visited[i] = False
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = 1e9

backtracking(0, 0)
print(answer)
