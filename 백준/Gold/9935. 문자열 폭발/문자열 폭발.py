import sys
input = sys.stdin.readline

s = input().strip()
boom = input().strip()

stack = []

for i in s:
  stack.append(i)
  if ''.join(stack[-len(boom):]) == boom:
    del stack[-len(boom):]

if not ''.join(stack):
  print("FRULA")
else:
  print(''.join(stack))
