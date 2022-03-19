t = int(input())

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

for _ in range(t):
  n = list(map(int,input().split())) # 처음 입력하는 수는 개수
  sum = 0
  for i in range(1, len(n)-1):
    for j in range(i+1, len(n)):
        sum += gcd(n[i],n[j])

  print(sum)