def recursion(s, left, right, total):
  if left >= right:
    return 1, total
  elif s[left] != s[right]:
    return 0, total
  else:
    return recursion(s, left + 1, right - 1, total+1)
  
def is_palindrome(s):
  return recursion(s, 0, len(s) - 1, 1)
  
t = int(input())

for _ in range(t):
  s = input()
  
  print(*is_palindrome(s))