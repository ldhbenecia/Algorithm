'''
n = input()
half_size = len(n) // 2

left = 0
right = 0
for i in n[:half_size]:
  left += int(i)
  
for i in n[half_size:]:
  right += int(i)

if left == right:
  print('LUCKY')
else:
  print('READY')
'''

n = input()
half_size = len(n) // 2

left = 0
right = 0
for i in range(half_size):
    left += int(n[i])

for i in range(half_size, len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
