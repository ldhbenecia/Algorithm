a = int(input())
b = int(input())
c = int(input())

temp = a * b * c
dp = [0] * 10

for i in str(temp):
    dp[int(i)] += 1

for i in dp:
    print(i)
