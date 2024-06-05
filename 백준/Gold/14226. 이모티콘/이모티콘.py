from collections import deque

def bfs():
  queue = deque([(1, 0, 0)])

  while queue:
    display, clip, time = queue.popleft()
    
    if display == s:
      return time
    
    if not visited[display][display]:
      queue.append((display, display, time + 1))
      visited[display][display] = True
    
    if clip > 0 and display + clip <= s and not visited[display + clip][clip]:
      queue.append((display + clip, clip, time + 1))
      visited[display + clip][clip] = True
    
    if display > 1 and not visited[display - 1][clip]:
      queue.append((display - 1, clip, time + 1))
      visited[display - 1][clip] = True
  
s = int(input())
visited = [[False] * (s + 1) for _ in range(s + 1)] # [화면][클립보드]
visited[1][0] = True # 이미 화면에 이모티콘 1개 입력

print(bfs())