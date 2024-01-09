t = int(input())
    
for _ in range(t):
  l, n = map(int, input().split())
  ants = [int(input()) for _ in range(n)]
  fast, slow = 0, 0

  for ant in ants:
    if ant > l // 2:
      if fast < l - ant:
        fast = l - ant
        
      if slow < ant:
        slow = ant
      
    else:
      if fast < ant:
        fast = ant
      
      if slow < l - ant:
        slow = l - ant
        
  print(fast, slow)
