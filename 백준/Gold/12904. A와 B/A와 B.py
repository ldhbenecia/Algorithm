import sys
input = sys.stdin.readline

s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))

while len(t) != len(s):
  if t[-1] == 'A':
    t.pop()
  elif t[-1] == 'B':
    t.pop()
    t.reverse()

if s == t:
  print(1)
else:
  print(0)
