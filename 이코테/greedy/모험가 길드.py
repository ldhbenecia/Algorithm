n = int(input())
adventurer = sorted(list(map(int, input().split())))

result = 0
count = 0

for i in adventurer:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)

'''
5
2 3 1 2 2

정답: 2
'''