import sys
input = sys.stdin.readline

s = input()

answer = ''
for i in s:
  if i.isalpha():
    if 'A' <= i <= 'Z':
      if 'A' <= i <= 'M':
        answer += chr(ord(i) + 13)
      else:
        answer += chr(ord(i) - 13)
    
    if 'a' <= i <= 'z':
      if 'a' <= i <= 'm':
        answer += chr(ord(i) + 13)
      else:
        answer += chr(ord(i) - 13)
  else:
    answer += i

print(answer)