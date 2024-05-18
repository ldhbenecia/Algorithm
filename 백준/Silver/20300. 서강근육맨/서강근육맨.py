n = int(input())
t = sorted(list(map(int, input().split())))

answer = []
if n % 2 != 0:
  answer.append(t.pop())

for i in range(len(t) // 2):
  answer.append(t[i] + t[-i-1])
  
print(max(answer))