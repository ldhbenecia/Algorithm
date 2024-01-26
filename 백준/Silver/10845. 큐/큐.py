import sys 
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
  command = input().split()
  
  if command[0] == "push":
    queue.append(command[1])
  if command[0] == "pop":
    if not queue:
      print(-1)
    else:
      print(queue.pop(0))    
  if command[0] == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
  if command[0] == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)
  if command[0] == "size":
    print(len(queue))
  if command[0] == "empty":
    if queue:
      print(0)
    else:
      print(1)
