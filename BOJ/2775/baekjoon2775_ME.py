t = int(input())

for _ in range(t):
  k = int(input()) # 층
  n = int(input()) # 호
  k0 = [i for i in range(1, n+1)] # 0층

  for _ in range(k):
    for j in range(1, n):
      k0[j] += k0[j-1] # 바로 전 호에 살고 있는 인원 + 바로 아래층 같은 호수에 살고 있는 인원

  print(k0[-1])