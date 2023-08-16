n, m = map(int,input().split())

hear_man = set()
see_man = set()

for _ in range(n):
  hear_man.add(input())
  
for _ in range(m):
  see_man.add(input())
  

nothing_man = sorted(list(hear_man & see_man))

print(len(nothing_man))

for i in nothing_man:
  print(i)