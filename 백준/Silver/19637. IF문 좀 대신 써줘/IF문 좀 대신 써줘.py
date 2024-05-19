import sys
input = sys.stdin.readline

def search(power):
  left = 0
  right = len(title_list) - 1
  
  if left > right:
    return title_list[left][0]
  
  while left <= right:
    mid = int(left + right) // 2
    
    if power <= int(title_list[mid][1]):
      right = mid - 1
    else:
      left = mid + 1
      
  return title_list[left][0]

n, m = map(int, input().split())
title_list = [input().split() for _ in range(n)]

for _ in range(m):
  char_power = int(input())
  print(search(char_power))
  