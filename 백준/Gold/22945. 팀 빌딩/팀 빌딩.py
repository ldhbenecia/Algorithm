import sys
input = sys.stdin.readline

n = int(input())
ability = list(map(int, input().split()))

max_team = -1e9
start = 0
end = n - 1

while start < end:
  between = end - (start + 1)
  max_team = max(max_team, between * min(ability[start], ability[end]))
  
  if ability[start] < ability[end]:
    start += 1
  else:
    end -= 1
    
print(max_team)