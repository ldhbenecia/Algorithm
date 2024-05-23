import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal_list = [list(map(int, input().split())) for _ in range(n)]
medal_list.sort()

k, kg, ks, kb = medal_list[k-1]
rank = 1

for nation, gold, silver, bronze in medal_list:
  if k == nation:
    continue
  if gold > kg or (gold == kg and silver > ks) or (gold == kg and silver == ks and bronze > kb):
    rank += 1
    
print(rank)
  