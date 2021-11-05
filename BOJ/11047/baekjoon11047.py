n, k = map(int,input().split())
cnt = 0
coin = []

for _ in range(n):
    coin.append(int(input()))

coin.reverse()

for i in coin:
    cnt += k // i
    k = k % i

print(cnt)