import sys

input = sys.stdin.readline
m = int(input())

array = set()

for i in range(m):
  command = list(input().split())
  
  if command[0] == "add":
    array.add(int(command[1]))
  
  elif command[0] == "remove":
    if int(command[1]) in array:
      array.remove(int(command[1]))
    
  elif command[0] == "check":
    if int(command[1]) in array:
      print(1)
    else:
      print(0)
  
  elif command[0] == "toggle":
    if int(command[1]) in array:
      array.remove(int(command[1]))
    else:
      array.add(int(command[1]))
    
  elif command[0] == "all":
    array = set([i for i in range(1, 21)])
    
  else:
    array = set()
    